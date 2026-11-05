#!/usr/bin/env python3
"""Finite checks for the photon-loss proofs and constrained reconstruction.

Exact rational checks are separate from floating-point LP illustrations.
This program does not establish the infinite-dimensional asymptotic theorem.
"""
from __future__ import annotations

import argparse
import json
import math
import platform
from fractions import Fraction
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import linprog
from scipy.special import eval_laguerre
from scipy.stats import binom


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def binomial_half(m: int) -> list[Fraction]:
    return [Fraction(math.comb(m, n), 2**m) for n in range(m + 1)]


def thin_exact(p: list[Fraction], eta: Fraction) -> list[Fraction]:
    return [sum((p[n] * math.comb(n, k) * eta**k * (1 - eta)**(n-k)
                 for n in range(k, len(p))), Fraction(0))
            for k in range(len(p))]


def exact_checks() -> dict:
    moment_checks = 0
    divergence_checks = 0
    mixture_checks = 0
    for m in range(2, 13):
        b = binomial_half(m)
        odd = [2*x if n % 2 else Fraction(0) for n, x in enumerate(b)]
        require(sum(b) == sum(odd) == 1, "normalization")
        require(sum((-1)**n*x for n,x in enumerate(b)) == 0, "binomial parity")
        require(sum((-1)**n*x for n,x in enumerate(odd)) == -1, "odd parity")
        for s in range(m):
            require(sum(Fraction(n**s)*x for n,x in enumerate(b)) ==
                    sum(Fraction(n**s)*x for n,x in enumerate(odd)), "moment matching")
            moment_checks += 1
        for eta in map(Fraction, ["1/4", "1/2", "3/4", "9/10", "1"]):
            qb, qo = thin_exact(b, eta), thin_exact(odd, eta)
            require(sum(qb) == sum(qo) == 1, "thinning normalization")
            difference = [qo[k]-qb[k] for k in range(m+1)]
            expected = [-eta**m * Fraction((-1)**k*math.comb(m,k), 2**m)
                        for k in range(m+1)]
            require(difference == expected, "signed PGF coefficient identity")
            tv = sum(abs(x) for x in difference)/2
            require(tv == eta**m/2, "exact total variation")
            chi = sum((qo[k]-qb[k])**2/qb[k] for k in range(m+1))
            formula = (eta/(2-eta))**m
            require(chi == formula, "exact chi-square identity")
            divergence_checks += 1
            for w in [Fraction(1,10), Fraction(1,3)]:
                tau = [Fraction(1,2), Fraction(1,2)] + [Fraction(0)]*(m-1)
                null = [(1-w)*tau[n]+w*b[n] for n in range(m+1)]
                alt = [(1-w)*tau[n]+w*odd[n] for n in range(m+1)]
                require(sum(n*null[n] for n in range(m+1)) ==
                        (1+w*(m-1))/2, "null energy")
                require(sum(n*alt[n] for n in range(m+1)) ==
                        (1+w*(m-1))/2, "alternative energy")
                require(sum((-1)**n*alt[n] for n in range(m+1)) == -w,
                        "alternative negative parity")
                q0,q1=thin_exact(null,eta),thin_exact(alt,eta)
                mixed_chi=sum((q1[k]-q0[k])**2/q0[k] for k in range(m+1))
                require(mixed_chi <= w*formula, "mixture chi-square contraction")
                mixture_checks += 1
    return {"moment_equalities":moment_checks,
            "exact_thinning_TV_chi_square_cases":divergence_checks,
            "energy_parity_mixture_bound_cases":mixture_checks}


def wigner_checks() -> dict:
    maximum_error=0.0
    checked=0
    for m in [1,2,3,5,8,12,20]:
        p=np.array([float(x) for x in binomial_half(m)])
        for radius in np.linspace(0,5,101):
            x=2*radius**2
            # Independent Fock/Laguerre expansion and closed positive expression.
            expanded=(2/math.pi)*math.exp(-x)*sum(
                p[n]*(-1)**n*eval_laguerre(n,2*x) for n in range(m+1))
            closed=(2/math.pi)*math.exp(-x)*(x**m/math.factorial(m))
            maximum_error=max(maximum_error,abs(expanded-closed))
            require(abs(expanded-closed)<2e-12,"Wigner/Laguerre identity")
            require(expanded>=-2e-12,"sampled null Wigner positivity")
            checked+=1
    return {"sampled_points":checked,"max_absolute_error":maximum_error,
            "meaning":"finite identity checks; global positivity is proved analytically"}


def thinning_matrix(cutoff: int, eta: float) -> np.ndarray:
    k=np.arange(cutoff+1)[:,None]
    n=np.arange(cutoff+1)[None,:]
    return binom.pmf(k,n,eta)


def parity_interval(q: np.ndarray, cutoff: int, eta: float, energy: float,
                    radius: float) -> tuple[float,float,float]:
    """Extrema over a finite energy-constrained l1 ball; q includes overflow."""
    d=cutoff+1
    channel=np.vstack([thinning_matrix(cutoff,eta),np.zeros((1,d))])
    require(q.shape==(d+1,),"histogram must include overflow")
    require(abs(q.sum()-1)<1e-10 and np.min(q)>=-1e-14,"histogram simplex")
    slack=np.eye(d+1)
    a=np.vstack([np.hstack([channel,-slack]),
                 np.hstack([-channel,-slack]),
                 np.r_[np.zeros(d),np.ones(d+1)][None,:],
                 np.r_[np.arange(d),np.zeros(d+1)][None,:]])
    b=np.r_[q,-q,radius,energy]
    equality=np.r_[np.ones(d),np.zeros(d+1)][None,:]
    parity=(-1.0)**np.arange(d)
    solutions=[]
    violation=0.0
    for sign in [1.,-1.]:
        obj=np.r_[sign*parity,np.zeros(d+1)]
        opt=linprog(obj,A_ub=a,b_ub=b,A_eq=equality,b_eq=[1.],
                    bounds=(0,None),method="highs",
                    options={"primal_feasibility_tolerance":1e-9,
                             "dual_feasibility_tolerance":1e-9})
        require(opt.success,"LP failure: "+opt.message)
        fitted=opt.x[:d]
        violation=max(violation,max(0.,float(np.abs(channel@fitted-q).sum()-radius)),
                      max(0.,float(np.arange(d)@fitted-energy)),
                      abs(float(fitted.sum()-1)))
        solutions.append(float(parity@fitted))
    return solutions[0],solutions[1],violation


def lp_checks() -> list[dict]:
    # A physical energy-one alternative, with input parity -1/4.
    m=5
    w=.25
    cutoff=32
    b=np.array([float(x) for x in binomial_half(m)])
    p=np.zeros(cutoff+1)
    p[:2]=(1-w)/2
    p[:m+1]+=w*b*(2*(np.arange(m+1)%2))
    truth=float(((-1.)**np.arange(cutoff+1))@p)
    require(abs(truth+.25)<1e-14 and abs(np.arange(cutoff+1)@p-1)<1e-14,
            "test input promise")
    output=[]
    for eta in [.5,.8,.95,1.]:
        q=np.r_[thinning_matrix(cutoff,eta)@p,0.]
        last_width=math.inf
        for radius in [1e-2,1e-4,1e-6]:
            lo,hi,violation=parity_interval(q,cutoff,eta,1.,radius)
            require(lo-2e-7<=truth<=hi+2e-7,"true input excluded by exact-data LP")
            require(hi-lo<=last_width+2e-7,"nested-radius interval monotonicity")
            require(violation<2e-7,"LP feasibility residual")
            if eta==1.:
                require(hi-lo<=2*radius+3e-7,"lossless l1 parity Lipschitz bound")
            last_width=hi-lo
            output.append({"eta":eta,"output_l1_radius":radius,
                           "input_cutoff":cutoff,"lower_parity":lo,
                           "upper_parity":hi,"interval_width":hi-lo,
                           "truth":truth,"max_constraint_violation":violation})
    # Explicit overflow: the fitted laws have zero mass there and must pay it.
    eta=.8
    q=np.r_[thinning_matrix(cutoff,eta)@p,0.]
    q[0]-=.01
    q[-1]=.01
    lo,hi,violation=parity_interval(q,cutoff,eta,1.,.021)
    require(violation<2e-7,"overflow LP feasibility residual")
    require(lo-2e-7<=truth<=hi+2e-7,"overflow mass not correctly charged")
    output.append({"eta":eta,"output_l1_radius":.021,"input_cutoff":cutoff,
                   "overflow_mass":.01,"lower_parity":lo,"upper_parity":hi,
                   "truth":truth,"max_constraint_violation":violation})
    return output


def exact_lower_bound_examples() -> list[dict]:
    c=math.log(5/4)
    rows=[]
    energy=1.
    for eta in [.5,.8,.95,1.]:
        for delta in [.2,.1,.05,.025]:
            m=math.floor((2*energy-1)/delta+1)
            log_bound=math.log(c/delta)+m*math.log((2-eta)/eta)
            rows.append({"energy":energy,"eta":eta,"parity_gap":delta,
                         "m":m,"common_mean":(1+delta*(m-1))/2,
                         "log_copy_lower_bound_from_chi_square":log_bound})
    return rows


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,
                        default=Path(__file__).with_name("results.json"))
    args=parser.parse_args()
    result={"environment":{"python":platform.python_version(),
                           "numpy":np.__version__,"scipy":scipy.__version__},
            "exact":exact_checks(),"wigner":wigner_checks(),
            "linear_programs":lp_checks(),
            "lower_bound_examples":exact_lower_bound_examples(),
            "scope":"Finite exact identities and finite-cutoff LP checks; no numerical proof of asymptotic minimax optimality."}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,allow_nan=False)+"\n")
    print(json.dumps({"status":"PASS","exact":result["exact"],
                      "wigner_points":result["wigner"]["sampled_points"],
                      "lp_examples":len(result["linear_programs"]),
                      "output":str(args.output)},indent=2))


if __name__=="__main__":
    main()
