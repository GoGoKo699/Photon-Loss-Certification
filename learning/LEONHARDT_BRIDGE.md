# From optical state measurement to photon-loss certification

A photon counter measures the light that reaches it. If some photons have already been lost, its data describe the received state, while the question may concern the source before attenuation. Knowing the transmission efficiency specifies the relation between those states. The statistical issue is how accurately that relation can be inverted from a finite number of copies.

The selected educational anchor is **Ulf Leonhardt, Measuring the Quantum State of Light (Cambridge University Press, 1997)**. Its optical-state, measurement, and reconstruction topics provide the entry point. This bridge fixes the repository's notation, works through a complete low-photon example, and explains the additional statistical arguments behind the [precision laws](../science/model.md). The [milestone map](MILESTONES.md) connects these steps to the full scientific account.

## 1. Verified reading pointers

The [publisher's front matter](https://assets.cambridge.org/97805214/97305/frontmatter/9780521497305_frontmatter.pdf) identifies the 1997 publication and gives the contents on printed pages vi–viii, corresponding to PDF pages 7–9. The following are verified section numbers and **printed starting pages**. The descriptions explain their role in this project; they are not quotations from the chapter text.

| Source pointer | Reading role in this project | Project continuation |
|---|---|---|
| §2.2.2, p. 21 | Describe one optical mode through its photon occupations. | The basis states, probabilities, and energy constraint in [the model](../science/model.md). |
| §3.1, p. 37 | Connect a state with its phase-space representation. | The repository's Wigner normalization and origin-parity target in [the model](../science/model.md). |
| §4.1.4, p. 79 | Interpret attenuation through a beam splitter; the project uses a vacuum environment. | The pure-loss channel and binomial count law in [the model](../science/model.md). |
| §4.2.1, p. 84 | Connect the optical state with detector outcomes. | Received photon counts and the finite measurement with overflow in [recovery, Section 3](../science/recovery.md#3-a-finite-estimator-with-confidence-and-overflow). |
| §5.2.2, p. 113 | Place photon statistics within the broader reconstruction setting. | The reduction to one count-dependent observable in [the model](../science/model.md). |
| §5.3.1, p. 132 | Connect detection loss with the inference problem. | The distinction between source and received parity in [the interpretation](../science/interpretation.md). |
| §5.3.4, p. 138 | Connect finite data with uncertainty in a reconstructed quantity. | The explicit finite-confidence upper bound in [recovery](../science/recovery.md) and the converse in [limits](../science/limits.md). |

The inspected publisher preview contains front matter, not these chapter bodies. It verifies the reading pointers but does not establish the book's detailed equations or normalization conventions. All formulas below use the repository's explicitly stated conventions and locally supplied derivations. The source's bibliographic identity is recorded under [Leo97](../references/REFERENCES.md#leo97).

## 2. Objects and conventions used here

The state $|n\rangle$ has exactly $n$ photons in the mode. For an arbitrary density operator $\rho$, its photon probabilities are

```math
p_n=\langle n|\rho|n\rangle,
\qquad
\sum_{n=0}^{\infty}p_n=1.
```

Coherences between different photon numbers may be present; the target and the photon-count measurement considered here depend only on these diagonal probabilities.

| Symbol | Meaning in this repository |
|---|---|
| $\hat n$, $n$ | Photon-number operator and an individual photon occupation. |
| $E$ | A known bound on the mean source photon number, $\mathrm{Tr}(\hat n\rho)\le E$. |
| $\eta$ | Known transmissivity of the pure-loss channel, with $0<\eta\le1$. |
| $q_k$ | Probability of receiving $k$ photons after that channel. |
| $N$ | Number of independent source copies consumed, not the photon number in a copy. |
| $\delta$, $\beta$ | Requested parity accuracy and allowed failure probability. |
| $\alpha$ | A phase-space point; it is distinct from the confidence parameter $\beta$. |

Photon parity assigns $+1$ to even occupations and $-1$ to odd occupations:

```math
\Pi=(-1)^{\hat n},
\qquad
\theta(\rho)=\mathrm{Tr}(\Pi\rho)
=\sum_n(-1)^np_n
=1-2p_{\mathrm{odd}}.
```

The project uses the quantum-optical convention

```math
W_\rho(0)=\frac{2}{\pi}\theta(\rho).
```

Thus negative parity is exactly a negative Wigner value at the origin, and parity error $\delta$ corresponds to Wigner-value error $2\delta/\pi$. This normalization is fixed by [the model](../science/model.md), rather than inferred from the source preview.

There is one useful notation distinction visible even in the contents. Leonhardt's §§3.2.1–3.2.2 identify phase-space functions denoted $Q$ and $P$. In this project,

```math
P(z)=\sum_n p_nz^n,
\qquad
Q(z)=\sum_k q_kz^k
```

are **probability generating functions of photon counts**. Their argument $z$ is an auxiliary complex variable, not a phase-space point, and these functions are different from the phase-space objects.

## 3. A complete example: loss changes the measured parity

Suppose the source is promised to belong to the family

```math
\rho_t=(1-t)|0\rangle\langle0|+t|1\rangle\langle1|,
\qquad 0\le t\le1,
```

where $t$ is unknown. Its mean photon number is $t$. Its source parity is

```math
\theta_{\mathrm{in}}=1-2t.
```

Vacuum stays vacuum under pure loss. A single photon reaches the receiver with probability $\eta$ and is lost with probability $1-\eta$. The lost mode is unobserved, so the received state is

```math
\mathcal L_\eta(\rho_t)
=(1-\eta t)|0\rangle\langle0|
+\eta t|1\rangle\langle1|.
```

The measured parity therefore has expectation

```math
\theta_{\mathrm{out}}=1-2\eta t.
```

For the concrete instance $t=3/4$ and $\eta=1/2$, the probabilities and parities are:

| State | Zero photons | One photon | Mean photon number | Parity |
|---|---:|---:|---:|---:|
| Source | $1/4$ | $3/4$ | $3/4$ | $-1/2$ |
| Received | $5/8$ | $3/8$ | $3/8$ | $1/4$ |

The source has $W_{\mathrm{in}}(0)=-1/\pi$, while the received state has $W_{\mathrm{out}}(0)=1/(2\pi)$. The sign has changed. Accurately averaging the received parity would converge to $1/4$; the input quantity being sought is $-1/2$.

### Correcting the finite-support example

Let $C$ be the number of one-photon outcomes among $N$ received copies. Then $C$ is binomial with success probability $\eta t$. The estimator

```math
\widehat\theta
=1-\frac{2C}{\eta N}
```

has expectation $1-2t$, so it estimates the source parity. At the displayed instance,

```math
\mathrm{Var}(\widehat\theta)
=\frac{4(\eta t)(1-\eta t)}{\eta^2N}
=\frac{15}{4N}.
```

A concentration bound also gives an accuracy guarantee uniformly over this family:

```math
\Pr \left\lbrace
|\widehat\theta-\theta_{\mathrm{in}}|>\delta
\right\rbrace
\le
2\exp \left[-\frac{N\eta^2\delta^2}{2}\right].
```

Indeed, a parity error larger than $\delta$ requires the empirical one-photon frequency $C/N$ to differ from $\eta t$ by more than $\eta\delta/2$; Hoeffding's inequality for Bernoulli samples gives the displayed bound. Consequently

```math
N\ge
\frac{2}{\eta^2\delta^2}\log\frac{2}{\beta}
```

suffices for failure probability at most $\beta$. At $\eta=1/2$, the coefficient is $8$. Known loss is therefore correctable with polynomial copy cost in this particular family.

The extra information is the promise that only zero and one photons can occur. A bound on the **mean** alone does not give that support promise. This difference is what the general theorem must address.

## 4. Why the same correction becomes unstable on the larger class

For a source occupation $n$, the received count $K$ has the binomial law

```math
\Pr\lbrace K=k\mid n\rbrace
=\binom nk\eta^k(1-\eta)^{n-k}.
```

Its generating identity is

```math
\mathbb E[a^K\mid n]=(1-\eta+\eta a)^n.
```

Choosing $a=1-2/\eta$ makes the right side $(-1)^n$. This suggests assigning the received count $K$ the inverse weight

```math
g(K)=\left(1-\frac2\eta\right)^K.
```

In the two-level example at $\eta=1/2$, these weights are simply $g(0)=1$ and $g(1)=-3$, reproducing the estimator above. With unrestricted photon number, their magnitudes grow without bound for every $\eta<1$. The conditional identity at each finite $n$ does not guarantee that averaging over an arbitrary source distribution gives a finite expectation or variance.

The second moment makes the dependence on the source tail explicit:

```math
\mathbb E[g(K)^2\mid n]
=\left(1-\eta+\eta\left(1-\frac2\eta\right)^2\right)^n
=\left(\frac4\eta-3\right)^n.
```

Controlling $\sum_n np_n$ does not control this exponential moment. The instability of these inverse parity weights is established in [Banaszek's analysis](../references/REFERENCES.md#ban99). The stronger moment conditions that make inverse estimation effective are treated in [tail promises](../science/tail-promises.md), including a sufficient exponential-moment condition for this unbiased estimator.

An unstable estimator alone does not prove that the task is hard: biased estimators, nonlinear fits, or different measurements might succeed. The project supplies both an estimator that works uniformly under the mean bound and a lower bound on every allowed procedure.

## 5. From optical reconstruction to the statistical theorem

### The observation determines a generating function on a smaller disk

Summing the binomial law over the source probabilities gives

```math
Q(z)=P(1-\eta+\eta z),
\qquad |z|\le1.
```

The received data therefore constrain $P$ on the disk with center $1-\eta$ and radius $\eta$. Source parity is the boundary value $P(-1)$. For every $\eta<1$, that point lies outside the observed disk, even though the source generating function is defined continuously on the closed unit disk.

This geometry explains the distinction between identifiability and accuracy. Exact knowledge of the received law determines the source generating function by analytic continuation. Finite data give an approximate law, and continuation can amplify that uncertainty. The object to quantify is how much the input parity can vary among states whose received laws are close.

### The mean bound gives the regularity needed for recovery

For two source laws $p,\widetilde p$ with mean at most $E$, let $f=P-\widetilde P$. Their first moments imply

```math
\sum_n n|p_n-\widetilde p_n|\le2E,
\qquad
|f'(z)|\le2E\quad\text{for }|z|\le1.
```

The derivative series converges uniformly, so the bound remains meaningful at the boundary. If the received laws differ by at most $\epsilon$ in $\ell_1$ distance, then $|f|$ is at most $\epsilon$ on the observed disk.

The additional analytic step in [recovery, Theorem R1](../science/recovery.md#theorem-r1-an-explicit-first-moment-modulus) is to continue a bound on **the derivative**, then integrate it to $-1$. Harmonic measure quantifies how the interior information constrains that derivative along the path. At fixed $E>0$ and $0<\eta<1$, the resulting parity uncertainty is bounded by a constant times $1/\log(1/\epsilon)$ as $\epsilon$ tends to zero.

The statistical step then estimates the received count law and fits an input distribution consistent with the data and the same mean bound. The continuity theorem controls every feasible fit's parity. [Theorem R2](../science/recovery.md#theorem-r2-finite-constrained-recovery-of-a-count-distribution) makes this finite, with an overflow outcome, a cutoff justified by the energy promise, and an explicit confidence bound. It does not apply an unstable inverse to a discarded tail.

### A physical hard pair makes the upper rate necessary

The mean promise permits a component with probability of order $\delta$ at photon numbers of order $1/\delta$. Its contribution to the mean can remain bounded while it carries the parity difference being estimated.

The construction in [limits](../science/limits.md) uses a binomial photon distribution and its odd-conditioned counterpart. After attenuation their distinguishing information decreases exponentially in the photon scale. Dilution produces the required small parity gap within the fixed mean budget. For certification, the null is a mixture with an explicitly nonnegative Wigner function everywhere, while the alternative has negative parity at the origin.

Both received states are diagonal in the photon basis. Any collective quantum measurement of their copies is consequently a classical postprocessing of photon-number strings. This supplies a lower bound even for receivers with unrestricted quantum processing after loss. It is a concrete use of established discrimination methods; its physical pair and accuracy scaling are proved in the canonical [lower-bound account](../science/limits.md).

## 6. The result reached by the bridge

At confidence $2/3$, fixed $E>0$, and transmissivity $\eta\in[\eta_0,1]$ for fixed $\eta_0>0$, the optimal source-parity copy budget satisfies

```math
\log N_{\mathrm{est}}
=\Theta_{E,\eta_0} \left(
\log\frac1\delta+\frac{1-\eta}{\delta}
\right).
```

For any fixed nonzero loss this is an exponential cost in $1/\delta$. At no loss, direct parity measurement has the sharper cost $\Theta_E(\delta^{-2})$. The same logarithmic-order law holds for distinguishing a globally Wigner-positive source from one with origin parity at most $-\delta$, provided the mean budget is fixed above $1/2$. The exact hypotheses and quantifiers are in [the model](../science/model.md).

The low-photon worked example and this worst-case law describe different amounts of source information. A support restriction can make correction easy. A mean bound alone permits rare high occupations. Fixed higher photon moments improve the exponential scale; a known exponential moment gives a polynomial upper bound, as shown in [the tail analysis](../science/tail-promises.md). These promises are quantitative information supplied to the procedure.

The optical anchor supplies the route through states, phase space, attenuation, and measurement uncertainty. The project supplies the precise experiment, the mean-constrained continuation bound, the finite reconstruction, and the all-measurement converse. Their research precedents and the limits of the source comparison are distinguished in [related work](../references/RELATED_WORK.md). The resulting theorem concerns a prescribed Wigner point and counts consumed copies; its constructive estimator can require large photon resolution and optimization dimension, as explained in [the physical interpretation](../science/interpretation.md).
