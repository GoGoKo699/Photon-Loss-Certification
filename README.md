# Photon-Loss Certification

How accurately can a source's Wigner negativity be certified when its light is observed only after photon loss?

This project determines the optimal copy cost of recovering a single-mode source's photon parity under a known mean-energy bound and known pure loss. The lower bound allows arbitrary collective quantum measurements on the received copies. Photon counting with a finite constrained reconstruction achieves the same asymptotic order.

## Main result

Let $E$ be the fixed mean source photon-number bound, $\eta$ the transmissivity, and $\delta$ the required input-parity accuracy. For $E>0$ and transmissivity bounded below by a positive constant,

$$
\log N_{\rm est}
=\Theta_{E,\eta_0}\!\left(
\log\frac1\delta+\frac{1-\eta}{\delta}
\right),
\qquad \eta\in[\eta_0,1].
$$

At any fixed $0<\eta<1$, this is an exponential copy cost in $1/\delta$. At $\eta=1$, direct parity measurement has the usual quadratic cost. For fixed $E>1/2$, the same order holds for distinguishing a globally Wigner-positive state from a state with input parity at most $-\delta$ at the origin. The convention is $W_\rho(0)=2\operatorname{Tr}(\Pi\rho)/\pi$.

| Question | Answer and proof route |
|---|---|
| Can joint quantum measurements avoid the obstruction? | The commuting hard pair gives a converse for every output POVM. [Limits](science/limits.md) |
| Can a regularized procedure attain the rate? | A derivative-continuation bound and finite constrained fit provide a matching upper. [Recovery](science/recovery.md) |
| How much loss permits polynomial copy complexity? | At fixed energy, the loss must be of order at most accuracy times the logarithm of inverse accuracy. [Precise theorem](science/model.md) |
| Do stronger photon-tail promises help? | Higher moments improve the rate; an exponential-moment promise gives a polynomial upper. [Tail promises](science/tail-promises.md) |
| What is the physical limitation? | The result measures what energy information alone guarantees, including rare high-photon-number sectors. [Interpretation](science/interpretation.md) |

The result matches exponential order, not the exact leading constant in the exponent. The promise concerns a prescribed phase-space point, and only copies received after loss are available. The reconstruction's computational cost and photon-number resolution are accounted for separately from its copy count.

## Read the science

Start with the [scientific overview](science/README.md), then the [model and main statements](science/model.md). The full proofs are organized into [limits](science/limits.md), [recovery](science/recovery.md), and [tail promises](science/tail-promises.md).

The [related-work comparison](references/RELATED_WORK.md) separates the known instability of inverse parity reconstruction and the inherited statistical methods from the mean-constrained minimax theorem proved here. The [bibliography](references/REFERENCES.md) provides primary sources.

## Learn the project

The [learning route](learning/README.md) connects optical state measurement to the precision law through [30 milestones](learning/MILESTONES.md). Its single educational anchor is Ulf Leonhardt's *Measuring the Quantum State of Light* (1997). The [source-to-project bridge](learning/LEONHARDT_BRIDGE.md) gives the relevant reading, a worked photon-loss example and the additional statistical and analytic ingredients supplied by this project.

## Reproduce the checks

```bash
python -m pip install -r verification/requirements.txt
python verification/verify_photon_loss.py
```

The [verification guide](verification/README.md) describes the exact rational identities, Wigner-function checks and finite linear-program examples. The [saved numerical report](verification/results.json) records their domains and environment. Finite checks support the implementation; the universal statements follow from the analytical proofs.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
