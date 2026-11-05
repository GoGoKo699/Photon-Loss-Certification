# What loss changes, and what an energy promise guarantees

The quantity of interest is the source parity before a known attenuation channel. Parity is a bounded observable, so with direct copies its expectation is easy to estimate: every photon-count outcome contributes either $+1$ or $-1$. The difficulty arises because the experiment measures a different state after loss.

## Why a calibrated channel can still be difficult to invert

Calibration identifies the binomial thinning matrix. Formal inversion replaces the bounded source-parity statistic by count weights $(1-2/\eta)^k$, whose absolute values grow with $k$ whenever $\eta<1$. This instability and its variance consequences are established in Banaszek's analysis; see [the source comparison](../references/RELATED_WORK.md).

An unstable unbiased estimator does not prove that the statistical task is hard. A biased or nonlinear procedure might succeed. The results here allow all such procedures and arbitrary collective quantum measurements, then match their best possible copy-complexity order with a finite photon-counting reconstruction.

The key distinction is between an identifiable parameter and a uniformly stable inverse. For every $\eta>0$, the received generating function determines the source generating function by analytic continuation. But the required continuation reaches the boundary value $P(-1)$ outside the observed loss disk. A first-moment bound controls one derivative, which yields an inverse modulus proportional to $1/\log(1/\epsilon)$. Therefore exponentially fine information about the output law can be needed to recover a modestly small source-parity difference. The [recovery proof](recovery.md) makes this statement quantitative.

## A rare component hides the parity difference

The [hard construction](limits.md) mixes a fixed benign state with a component of weight $w$ whose photon number is of order $m$. It chooses $w$ of order the requested parity gap $\delta$ and $m$ of order $E/\delta$. The mean cost remains bounded because the large photon number occurs rarely.

Before loss, an odd-conditioned binomial component and its unconditioned counterpart have a definite parity difference. After loss their statistical distance decreases exponentially in $m$. The two states agree on low photon moments, and their output density operators commute. Collective output measurements therefore have no hidden noncommuting observable that restores the missing distinction.

For the certification version, the null has a Wigner function nonnegative throughout phase space. The alternative has a negative value at the origin. This turns the recovery obstruction into a statement about certifying source nonclassicality, while retaining an explicit physically valid null state.

The construction depends on the requested accuracy. The theorem does not assert that one fixed source remains a hardest instance at every precision. It also does not imply an exponential burden for every finite-cutoff, Gaussian, parametric or exponentially tailed source family. Such promises can exclude the rare high-photon components. The [tail analysis](tail-promises.md) quantifies this dependence rather than treating all finite-energy descriptions as interchangeable.

## Two useful loss scales

Write $\nu=1-\eta$. The uniform minimax theorem identifies

```math
\nu=O \left(\delta\log\frac1\delta\right)
```

as the loss scale compatible with polynomial copy complexity at fixed energy. This allows regularized inverse reconstruction.

A stricter scale lets the experimenter ignore the correction altogether. Couple a source count $n$ to the received count by independently deleting each photon with probability $\nu$. The two parity values differ only if an odd number of photons is deleted. Hence

```math
|\theta(\rho)-\theta(\mathcal L_\eta(\rho))|
\leq 2\sum_n p_n\Pr\lbrace \text{at least one deletion}\mid n\rbrace
\leq2\nu E.
```

If $\nu E\leq\delta/4$, the loss bias is at most $\delta/2$. The empirical mean of received parities has statistical error at most $\delta/2$ with failure probability at most $\beta$ when

```math
N\geq\frac{8}{\delta^2}\log\frac2\beta,
```

by Hoeffding's inequality for variables in $[-1,1]$. Thus direct uncorrected parity already achieves the target accuracy in this regime. The direct-measurement bias scale and the polynomial-complexity boundary are different: the region between them is precisely where correction can help without requiring a superpolynomial number of copies.

## Statistical and computational resources

The minimax theorem charges source copies. The finite upper bound also specifies a reconstruction that can actually be written as a linear program, so it is not merely a nonconstructive continuity statement. Its input cutoff may, however, be exponentially large in inverse accuracy under the mean-energy promise. The matrix contains binomial probabilities, and the required numerical tolerance can be exponentially small. No polynomial-time-in-$1/\delta$ reconstruction claim is made in the fixed-loss regime.

Photon-number resolution is likewise explicit. The statistical experiment permits photon counting, with finite overflow handling in the construction. It does not assume a hard physical source cutoff. A detector with a prescribed bounded resolution gives a different observation model unless its unresolved tail is included in the error budget.

The general collective-measurement lower charges only copies and makes no favorable detector restriction. Additional output hardware cannot defeat that lower within the stated access model. Access before loss, environment monitoring, source-specific alternative preparations, or protection during transmission can change the available information and are not covered by that converse.

## Reading the main conclusion

At any fixed positive loss, the optimal worst-case parity precision falls only as the inverse logarithm of available copies, up to constants at fixed energy and confidence. At zero loss it falls as the inverse square root. The uniform theorem describes the transition when loss decreases with the desired error.

This is a quantitative limit on what a mean-energy promise alone can certify about the source. Its physical content is the combination of a valid nonclassicality promise, a lower bound covering every output measurement, and a recovery procedure that matches the order. The analytical machinery and the longstanding warning about unstable loss inversion are attributed separately in [related work](../references/RELATED_WORK.md).
