# Related work

This repository studies inference about an **input** optical state when only copies that have already passed through a known pure-loss channel are available. The target is its photon parity, equivalently its Wigner function at a prescribed origin. The state has a uniform bound on mean photon number. The lower bounds allow every collective measurement on the received copies; the upper bounds use photon counting and a constrained fit.

For fixed positive mean-photon budget and fixed transmissivity strictly between zero and one, the proved copy complexity has logarithm proportional to the inverse requested parity accuracy. The corresponding certification problem distinguishes a globally Wigner-positive state from a state with a specified negative origin value. Its energy budget must exceed one half. The statements concern exponential order, not an exact leading exponential constant. The mathematical arguments are given in [recovery](../science/recovery.md) and [limits](../science/limits.md).

## Comparison at a glance

| Earlier work | Established result relevant here | Additional question addressed here |
|---|---|---|
| [Banaszek](REFERENCES.md#ban99) | Inverse-loss parity weights are unstable at every nonunit efficiency. | What rate remains optimal after allowing bias, regularization, and all output measurements? |
| [Butucea–Guţă–Artiles](REFERENCES.md#bga07) | Minimax pointwise Wigner estimation from noisy homodyne data on fixed smoothness classes. | What does a mean-photon bound alone guarantee, without stronger uniform tail regularity? |
| [Polyanskiy–Suresh–Wu](REFERENCES.md#psw17) | Mixture-estimation duality and sharp lossy population-coordinate recovery. | What is the sharp modulus for the boundary parity functional under a first-moment constraint? |
| [Takagi–Tajima–Gu](REFERENCES.md#ttg23) | General noisy-pair distinguishability bounds for mitigation. | Which physical pair yields the mean-energy parity rate and a globally Wigner-positive null? |
| [Fawzi–Oufkir–Salzmann](REFERENCES.md#fos26) | Binary-measurement fidelity estimation, with published photon-loss bias bounds. | Can fixed loss be inverted to arbitrarily small error, and at what optimal copy cost? |
| [Mele et al.](REFERENCES.md#mele25) | Energy-constrained tomography from direct state copies. | How does compulsory loss change inference even for a single observable of one mode? |

## 1. Instability of loss-compensated parity is established

[Banaszek](REFERENCES.md#ban99), Section III, Eq. (20), reconstructs parity from photocount frequencies with weights $(1-2/\eta)^k$. Their magnitudes grow with $k$ for every $\eta<1$. Eqs. (21)–(22) quantify the resulting variance for coherent and thermal states, including failures of convergence. The familiar fifty-percent efficiency threshold for individual inverse-Bernoulli probabilities therefore does not protect parity reconstruction.

That paper establishes the central physical instability. Here the question is the optimal finite-error risk after permitting all biased and nonlinear reconstructions and all collective output measurements. An exploding variance for a particular inverse estimator does not by itself establish that risk. The matching constrained-recovery upper bound is necessary to identify the optimal accuracy dependence.

[Wu–Li–Peng–Guo](REFERENCES.md#wlpg11) likewise identify photon-to-photoelectron inversion as an ill-posed infinite binomial-mixture problem and propose Bayesian coarse graining. This comparison is limited to their accessible publisher abstract and introduction. Their unavailable full text is not being treated as a completed theorem-level comparison.

## 2. Noisy Wigner minimax theory uses a different uniform promise

[Butucea–Guţă–Artiles](REFERENCES.md#bga07) study inefficient random-phase homodyne observations. Their fixed classes $\mathcal A(\beta,r,L)$, $0<r\le2$, impose an exponentially weighted Fourier-square bound. Section 3 connects such regularity with photon moments of the form $\mathrm{Tr}\rho\exp(a\hat n^{r/2})<\infty$. Theorem 1 gives pointwise minimax rates through a bias–noise balance; the rate depends on the fixed class parameters.

A mean bound alone does not place all admissible states in one of those fixed classes. The difficult states here can put probability of order $\delta$ at photon numbers of order $1/\delta$, keeping their mean bounded while stronger moments grow. Letting the smoothness parameter tend to zero in the earlier theorem does not supply a uniform theorem for this class. Moreover, its lower bound concerns estimators of homodyne data; an all-measurement converse requires a separate argument. Regularization, minimax analysis, and severe inverse instability themselves are established ingredients.

## 3. Population recovery supplies the closest statistical framework

[Polyanskiy–Suresh–Wu](REFERENCES.md#psw17), Theorem 4, relates the minimax risk of a linear functional of a finite mixing distribution to a constrained modulus for the observation matrix. Its proof uses linear-program duality and a two-point testing lower bound. Their lossy-population analysis also expresses the binomial observation map by composing a probability generating function with an affine map and controls continuation through complex analysis.

The difference that matters is the functional and its uniform constraint. Writing $P(z)=\sum_n p_nz^n$, the observed count law has generating function

```math
Q(z)=P(1-\eta+\eta z).
```

Their solved coordinate problem concerns $P(0)$. Here parity is $P(-1)$, a boundary value of an unbounded-support generating function. The observation disk contains zero once $\eta\ge1/2$, but it excludes $-1$ for every $\eta<1$. A first-moment promise supplies the extra derivative bound needed at that boundary.

The general statistical reduction and continuation method are inherited. The rate here requires an additional modulus calculation: for two mean-bounded laws, apply continuation to the **derivative** of their generating-function difference and then integrate to $-1$. This gives an inverse-logarithmic bound without an extra logarithmic factor in the sample exponent. Theorem 4 does not evaluate this moment-constrained boundary modulus, and Proposition 9's solved coordinate rate cannot be substituted for it. The method remains a short adaptation of classical complex analysis, rather than a new general continuation principle; [Trefethen](REFERENCES.md#tre20) provides further background.

## 4. Quantum mitigation converses and photonic cancellation

[Takagi–Tajima–Gu](REFERENCES.md#ttg23), Theorem 1, already gives general sample lower bounds by comparing states whose ideal observable values differ but whose noisy versions are difficult to distinguish. The converse here is a concrete application of that established principle. Its physical calculation uses binomial Fock mixtures, an exact thinned divergence, and a rare high-photon component that respects the energy bound. Both received states commute, so their count strings contain all information relevant to the binary test; arbitrary collective measurements cannot remove the obstruction.

[Taylor et al.](REFERENCES.md#tbkk24) derive and implement inverse-loss error cancellation through signed combinations involving noiseless amplification and photon subtraction. They analyze bias and sampling overhead, including source-dependent simplifications. This establishes that expectation values can be corrected at a sampling cost. The present theorem quantifies the optimal worst-case cost under only a mean bound and a specified access model. It permits arbitrary processing after loss, with failed branches charged to the copy budget. Additional preparations or operations before the compulsory channel would change that model.

## 5. Modern fidelity estimation and energy-constrained learning

[Fawzi–Oufkir–Salzmann](REFERENCES.md#fos26) primarily estimate fidelity to a known pure target from binary measurements. Their **published Appendix B explicitly treats photon loss** under an energy constraint. It bounds the forward channel disturbance and the induced bias of the uncorrected fidelity estimator; Eqs. (B4)–(B5) require the bias budget to fit within the requested accuracy. This appendix is absent from the inspected arXiv v1, so the published version is essential to the comparison.

That robustness statement and the present inversion theorem answer different accuracy questions. At fixed nonzero loss, reducing sampling error does not remove the uncorrected estimator's bias. Here regularized inference recovers the input parity to arbitrary accuracy, with a quantified diverging cost.

[Mele et al.](REFERENCES.md#mele25) derive energy-constrained continuous-variable tomography bounds from direct copies; at a fixed number of modes their main bounds have polynomial accuracy dependence. Those direct-access rates cannot simply be transferred through the unstable inverse attenuator. The present single-mode, single-observable result isolates the cost imposed by that compulsory channel.

## 6. Wigner-negativity witnesses and the certification promise

[Chabaud et al.](REFERENCES.md#crw21) construct operational witnesses using finite Fock observables, including truncated odd-photon probabilities for Wigner negativity. [Chabaud–Emeriau–Grosshans](REFERENCES.md#ceg21) optimize witness thresholds over Wigner-positive states and prove completeness of a witness family. These are relevant certification methods; their existence does not imply a uniform inverse-loss accuracy rate from a mean bound alone.

The null used here is globally Wigner-positive, not merely nonnegative at the origin. A half-attenuated Fock state has a nonnegative Wigner function and supplies an explicit hard null component. The alternative has negative parity of a prescribed depth at the origin. This is a test at a known phase-space point; searching for an unknown negative region or estimating total negative Wigner volume is outside the theorem.

## Scope of the result

The established ingredients include the Wigner–parity relation, binomial loss, inverse-weight instability, mixture-estimation duality, analytic continuation, and noisy-state testing bounds. The result analyzed here combines a sharp first-moment boundary modulus with a physical hard pair to obtain matching exponential order and a uniform weak-loss crossover. It does not claim that every fixed laboratory state family has this cost: finite support, uniformly bounded higher moments, or exponential tails supply additional information. The role of such promises is treated separately in [tail assumptions](../science/tail-promises.md).
