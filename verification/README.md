# Reproduce the finite checks

The analytical proofs establish the infinite-dimensional minimax laws. This directory checks exact hard-family identities, a finite grid of Wigner identities, and the finite linear-program constraints used for recovery. It does not infer an asymptotic rate by fitting a numerical curve.

## Run

Use Python 3.12 or later and the pinned numerical dependencies:

```bash
python -m pip install -r verification/requirements.txt
python verification/verify_photon_loss.py
```

Run these commands from the repository root. The script writes `verification/results.json`; use `--output /path/to/results.json` for a separate report. The saved report records the actual Python, NumPy and SciPy versions. Assertions are implemented as explicit runtime checks, so Python's optimization flag does not disable them.

## What is checked

| Check | Domain | Evidence produced |
|---|---|---|
| Moment agreement | Binomial/odd-conditioned pairs for integers 2 through 12 | 77 exact rational equalities through degree one below the binomial parameter |
| Thinning, total variation and chi-square | The same pairs at transmissivities 1/4, 1/2, 3/4, 9/10 and 1 | 55 exact rational cases, including coefficient signs and normalization |
| Energy, parity and mixture bound | Two dilution weights for each pair and transmissivity | 110 exact rational checks of the energy promise, parity gap and chi-square upper bound |
| Wigner identity | Seven binomial parameters and 101 radii each | 707 floating-point comparisons between the Fock/Laguerre sum and the explicit positive expression |
| Constrained reconstruction | Four transmissivities, three output tolerances, and one overflow example | 13 finite linear-program examples with feasibility, containment and nesting checks |

The exact checks use Python's rational `Fraction` arithmetic. The Wigner calculation uses a separate Laguerre-polynomial expansion and tolerates an absolute discrepancy below `2e-12`; sampled nonnegativity supports the implementation, while global nonnegativity follows from the closed expression in [the proof](../science/limits.md).

The linear programs use SciPy's HiGHS solver with feasibility and dual tolerances of `1e-9`. The script independently evaluates normalization, energy and full observation residuals after solving; the acceptance threshold is `2e-7`. These are floating-point checks of finite examples, not certified rational solutions of the full statistical construction. The [recovery proof](../science/recovery.md) gives the analytical error budgets and the conditions required of certified approximate channel coefficients.

## A finite reconstruction example

The example source is the odd-conditioned binomial component with parameter five, mixed at weight one quarter into the equally weighted vacuum/one-photon state. Its mean is one photon and its parity is minus one quarter. The fitted input distributions have support from zero to 32 photons and mean at most one. The center of the observation ball is the exact thinned distribution; these are deterministic sensitivity examples, not simulated confidence intervals.

At output-distribution l1 radius `0.01`, the fitted parity ranges are:

| Transmission | Lower parity | Upper parity |
|---|---:|---:|
| 0.50 | −0.267778 | 0.218920 |
| 0.80 | −0.260127 | −0.186212 |
| 0.95 | −0.258438 | −0.233324 |
| 1.00 | −0.258000 | −0.240000 |

The true parity lies in every interval. At lower transmission, the same observation tolerance can admit a wider range of source parities. Smaller observation balls give nested intervals. The overflow example moves `0.01` of observed mass into the overflow category and verifies that this mass is charged in the l1 residual, rather than omitted.

The cutoff 32 is chosen for a small reproducible optimization example. It is not the cutoff prescribed by the uniform theorem at these tolerances, and these intervals do not bound every infinite-support source. The theorem chooses its cutoff from energy and the desired output tolerance and includes truncation in its proof.

## Lower-bound examples

The report also evaluates the explicit certification lower bound for mean energy one, four transmissivities and four parity gaps. It uses the conservative testing constant `log(5/4)` from [the limits proof](../science/limits.md). These values are lower bounds, not estimates of the exact optimal copy count. No leading exponential constant is inferred.

## Interpretation of a passing run

A pass confirms the listed identities on their stated finite domains and the numerical optimization's reported constraints. The analytic continuation, all-measurement converse, uniform limiting regimes and stronger-tail theorems require their proofs. A passing run does not verify experimental loss calibration, physical detector resolution or computational efficiency at the large cutoffs required by the worst-case upper bound.
