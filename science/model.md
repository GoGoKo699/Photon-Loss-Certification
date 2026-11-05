# Model, tasks and precision laws

Photon counting gives a direct measurement of photon parity when every photon reaches the detector. With loss, the received count is a binomially thinned version of the source count. Knowing the transmission efficiency identifies this channel, but does not by itself make its inverse statistically stable. This project determines the optimal copy cost of recovering one source parity under a mean-energy promise.

The main result is a worst-case statement about what this promise guarantees. Both arbitrary collective quantum measurements and biased, nonlinear reconstruction procedures are included. The constructive upper uses separate photon counting followed by a finite constrained fit. The [lower-bound proof](limits.md) and [recovery proof](recovery.md) give the two sides; [physical interpretation](interpretation.md) explains their scope.

## State, energy and channel

Let the single-mode Fock space have basis $\{|n\rangle:n\geq 0\}$, number operator $\hat n$, and parity operator $\Pi=(-1)^{\hat n}$. The unknown source state belongs to

$$
\mathcal S_E=\{\rho\geq0:\operatorname{Tr}\rho=1,\quad
\operatorname{Tr}(\hat n\rho)\leq E\}.
$$

The bound $E$ is supplied to the procedure. No Gaussian, finite-support or exponential-tail assumption is made. States in this class can have small probability at arbitrarily large photon number. Coherence in the Fock basis is allowed.

The experimenter receives independent copies of $\mathcal L_\eta(\rho)$, where $\mathcal L_\eta$ is the single-mode pure-loss channel with known transmissivity $0<\eta\leq1$. An equivalent physical definition is a beam splitter coupling the source to a vacuum environment, followed by tracing out the environment. Each copy is prepared independently in the same unknown state.

Only the outputs are available. There is no control of the source before loss, no access to the loss environment or a record of lost photons, and no oracle that coherently prepares the unknown input state. An experimenter may attach known ancillas, adapt later measurements to earlier outcomes, or measure all received copies jointly. All source copies consumed, including unsuccessful attempts, count toward the copy budget $N$.

These assumptions separate statistical recovery from protection during transmission or source-dependent error cancellation. See [related work](../references/RELATED_WORK.md) for the corresponding distinctions in existing reconstruction and error-mitigation protocols.

## Photon counting and the generating function

Write $p_n=\langle n|\rho|n\rangle$. The received photon-count law is

$$
q_k=(T_\eta p)_k
=\sum_{n=k}^\infty\binom nk\eta^k(1-\eta)^{n-k}p_n.
$$

This formula holds even if the source has off-diagonal coherences. For example, the loss Kraus operators map $|n\rangle$ to a multiple of $|n-\ell\rangle$ when $\ell$ photons are lost; a diagonal output matrix element receives contributions only from diagonal input elements. In particular,

$$
\sum_k kq_k=\eta\sum_n np_n\leq\eta E.
$$

For the probability generating functions $P(z)=\sum_n p_nz^n$ and $Q(z)=\sum_kq_kz^k$,

$$
Q(z)=P(1-\eta+\eta z),\qquad |z|\leq1.
$$

The target is

$$
\theta(\rho)=\operatorname{Tr}(\Pi\rho)=P(-1).
$$

Use the quantum-optical convention

$$
W_\rho(\alpha)=\frac2\pi
\operatorname{Tr}\!\left[D(-\alpha)\rho D(\alpha)\Pi\right],
\qquad W_\rho(0)=\frac2\pi\theta(\rho).
$$

Thus an additive parity error $\delta$ corresponds to Wigner-value error $2\delta/\pi$ at the origin. All accuracy statements below use the parity normalization. The same prescribed origin is used throughout the upper and lower bounds.

## Task 1: recover the source parity

For $0<\delta<1$ and failure probability $0<\beta<1/2$, define $N_{\rm est}(E,\eta,\delta,\beta)$ as the smallest integer $N$ for which an output measurement and estimator $\widehat\theta$ obey

$$
\sup_{\rho\in\mathcal S_E}
\Pr_\rho\{|\widehat\theta-\theta(\rho)|>\delta\}\leq\beta.
$$

The minimization is over all procedures using at most $N$ received copies. A fixed-budget collective POVM subsumes adaptive and randomized output procedures with the same worst-case budget. The estimator may be biased. The resource is copies, not arithmetic operations or a restriction to a linear inverse estimator.

Unless explicitly displayed, confidence is fixed at $1-\beta=2/3$. The recovery proof gives a finite construction with an explicit failure-probability parameter. Changing between fixed confidence levels changes constants, not the asymptotic laws below.

### Theorem: mean-energy parity recovery

Fix $E>0$ and $0<\eta_0\leq1$. There are positive constants $c,C,\delta_0$, depending only on $E,\eta_0$, such that for every $0<\delta<\delta_0$ and every $\eta\in[\eta_0,1]$,

$$
c\left[\log\frac1\delta+\frac{1-\eta}{\delta}\right]
\leq
\log N_{\rm est}(E,\eta,\delta,1/3)
\leq
C\left[\log\frac1\delta+\frac{1-\eta}{\delta}\right].
$$

For any fixed $0<\eta<1$, this gives

$$
N_{\rm est}(E,\eta,\delta,1/3)
=\exp\!\left[\Theta_{E,\eta}(\delta^{-1})\right].
$$

At $\eta=1$, direct parity measurement and the parametric lower bound give the sharper statement $N_{\rm est}=\Theta_E(\delta^{-2})$. The uniform logarithmic theorem does not claim the exact exponent of every polynomial in a varying-loss regime, or the leading constant in a fixed-loss exponential.

The hard quantum family is diagonal in the Fock basis. Its received copies commute, so measuring photon number loses no discrimination information on that family. This gives the lower bound for arbitrary collective quantum measurements. For the upper bound, source parity and received photon counts depend only on $p$, so a classical reconstruction works for every state in $\mathcal S_E$, including coherent states and coherent superpositions. These two observations establish the quantum minimax order without assuming that all optimal quantum procedures are photon counting.

## Task 2: certify a prescribed negative Wigner value

For fixed $E>1/2$, consider the promise problem

$$
H_0:\quad \rho\in\mathcal S_E,\quad W_\rho(\alpha)\geq0
\text{ for every }\alpha,
$$

$$
H_1:\quad \rho\in\mathcal S_E,\quad\theta(\rho)\leq-\delta.
$$

Define $N_{\rm cert}(E,\eta,\delta,\beta)$ as the least fixed copy budget for a test with both worst-case type-I and type-II errors at most $\beta$. States satisfying neither promise impose no requirement on this test. A globally nonnegative Wigner function implies $\theta(\rho)\geq0$, so estimating parity to accuracy $\delta/3$ and thresholding at $-\delta/2$ supplies an upper bound.

### Theorem: positive-null certification

For every fixed $E>1/2$ and $\eta_0>0$, the same uniform logarithmic law holds:

$$
\log N_{\rm cert}(E,\eta,\delta,1/3)
=\Theta_{E,\eta_0}\!\left(
\log\frac1\delta+\frac{1-\eta}{\delta}\right),
\qquad \eta\in[\eta_0,1].
$$

Here $\delta$ tends to zero with $E,\eta_0$ fixed. Keeping the energy dependence visible, the hard-family lower exponent is proportional to $(E-1/2)(1-\eta)/\delta$, whereas the recovery upper uses $E(1-\eta)/\delta$. This theorem does not assert a uniform matching energy law as $E$ approaches $1/2$ with $\delta$.

The threshold on $E$ is necessary for a nonempty origin-negative alternative: if $p_{\rm odd}=\sum_{n\ \rm odd}p_n$, then

$$
\theta=1-2p_{\rm odd},\qquad
\sum_n np_n\geq p_{\rm odd}.
$$

Thus $\theta\leq-\delta$ requires $E\geq(1+\delta)/2$. The lower construction obeys this requirement and uses a null with an explicitly nonnegative Wigner function everywhere, not merely nonnegative parity at the origin.

This is a certification promise at one prescribed point. A test that searches all phase space for an unspecified negative point solves a different task; no matching search upper bound is claimed here.

## The loss budget and stronger tail promises

Let $\eta=\eta(\delta)\geq\eta_0$ and keep $E$ fixed. The uniform theorem gives a polynomial bound in $1/\delta$ exactly when

$$
1-\eta(\delta)=O\!\left(\delta\log\frac1\delta\right).
$$

If the ratio $(1-\eta)/(\delta\log(1/\delta))$ tends to infinity, the required copy count grows faster than every fixed polynomial. If that ratio is merely unbounded, no single uniform polynomial bound covers the whole sequence; a superpolynomial subsequence follows. This distinction matters for oscillating loss schedules.

The first-moment promise determines this rate. The [tail-promise analysis](tail-promises.md) treats fixed higher photon moments and exponential moments, showing how stronger source information improves recovery. These are different model classes, not assumptions silently used in the main theorem.

## Notation and proof dependencies

| Symbol | Meaning |
|---|---|
| $\hat n$ | Source photon-number operator |
| $E$ | Known upper bound on mean source photon number |
| $\eta$, $\nu=1-\eta$ | Known transmissivity and loss probability |
| $N$ | Number of consumed source copies |
| $p$, $q=T_\eta p$ | Source and received photon-count distributions |
| $\theta=P(-1)$ | Input parity, equal to $\pi W(0)/2$ |
| $\delta$ | Parity accuracy or certified negative parity gap |
| $\epsilon$ | Auxiliary output-distribution $\ell_1$ tolerance |
| $\beta$ | Failure-probability budget |

The [limits](limits.md) page proves the hard-pair identities, positive-null construction, statistical converse and parametric bound. The [recovery](recovery.md) page proves the inverse modulus, finite estimator and uniform upper. Combining those statements proves the two main theorems. The [verification route](../verification/README.md) supplies finite numerical checks; these check the formulas and reconstruction implementation, while the universal and asymptotic conclusions rest on the analytical proofs.
