# Scientific account

The experiment receives copies of an unknown single-mode optical state after a known photon-loss channel. The goal is to recover the source parity, or to certify a negative source Wigner value at the prescribed origin, using only an energy or photon-tail promise.

The central result gives matching upper and lower copy-complexity orders. With a fixed mean-energy budget and any fixed nonzero loss, the optimal cost is exponential in inverse parity accuracy. A uniform weak-loss theorem identifies the loss budget compatible with polynomial copy complexity. The result allows all collective quantum measurements, while a photon-counting reconstruction attains the order.

## Reading route

1. [Model and precision laws](model.md): the access model, copy resource, estimation and certification promises, main statements and notation.
2. [Statistical limits](limits.md): the explicit positive-null hard pair, exact thinned divergence, collective-measurement converse and endpoint checks.
3. [Recovery from photon counts](recovery.md): the derivative continuation theorem, finite-confidence constrained fit, overflow handling and uniform loss bounds.
4. [Stronger photon-tail promises](tail-promises.md): fixed higher moments, exponential moments and the resulting improved recovery rates.
5. [Physical interpretation](interpretation.md): what a mean-energy promise guarantees, the rare high-photon sector, two loss scales and computational costs.

For attribution, read [related work](../references/RELATED_WORK.md) and the [bibliography](../references/REFERENCES.md). For independent finite checks of the formulas and optimization, use [verification](../verification/README.md).

For an optical introduction and a structured route through the argument, use the [Leonhardt bridge](../learning/LEONHARDT_BRIDGE.md) and [30-milestone map](../learning/MILESTONES.md).

## How the proofs fit together

The lower bound starts with Fock-diagonal states whose parities differ while their low moments agree. Loss makes their received count distributions exponentially close. Diluting the hard component keeps the source mean bounded. One member has a globally nonnegative Wigner function, so the same construction gives a certification converse. Since the received states commute, no collective POVM has more discrimination information than the full photon-count string.

For the upper bound, the output count distribution controls the source generating function on a disk inside its analytic domain. The mean-energy promise bounds its derivative. A harmonic-measure estimate followed by integration controls the parity boundary value. A finite linear program fits an energy-bounded input distribution to the observed finite histogram, including overflow. The inverse-continuity bound then controls its parity error.

These arguments establish the rate for a prescribed point and a known channel. Each proof page states its finite constants and additional assumptions. Numerical checks confirm finite examples; they do not replace the universal arguments.
