# Thirty milestones through photon-loss certification

This map connects the optical experiment, the statistical obstruction, and the constructive recovery theorem. Its **13 background/preliminaries milestones** assemble the optical objects, probability tools, and analytic framework. Its **17 narrative/innovation milestones** develop the hard family and the recovery argument separately, then join them into the loss crossover, stronger-tail results, and their physical meaning. The allocation reflects the project's combination of quantum optics, statistical inference, and complex analysis.

Within each phase, the route moves from individual objects and mechanisms to the whole argument. The map identifies understanding targets and dependencies; complete proofs remain in the linked scientific pages.

**L97** denotes the single educational anchor, Ulf Leonhardt's *Measuring the Quantum State of Light* (1997). The [Leonhardt bridge](LEONHARDT_BRIDGE.md) gives the verified section locations, notation translation, and research-level steps supplied by this project. The section pointers below follow that bridge; the project's own pages specify its conventions and exact claims. Research citations provide attribution and proof context, rather than additional educational anchors.

Throughout, $\hat n$ is photon number, $N$ counts consumed copies, $\eta$ is known transmissivity, $\nu=1-\eta$, $\delta$ is source-parity accuracy, and $\epsilon$ is an output-distribution $\ell^1$ tolerance.

## Phase I: background and preliminaries — M01–M13

### M01. Photon number and state

- **Central question:** What information does a single mode's photon-number distribution contain?
- **Understanding target:** Connect the Fock basis, a normalized density operator, the probabilities $p_n$, and the mean $\operatorname{Tr}(\hat n\rho)$. Distinguish a general state from its diagonal photon statistics; allowing coherence does not remove the usefulness of those statistics.
- **Dependencies and story role:** None within this map; establishes the local physical objects.
- **Conceptual connection:** Operator expectations become probability functionals when the measured observable is diagonal.
- **Sources:** L97 §2.2.2; [Model: state, energy and channel](../science/model.md).

### M02. A bounded observable on an unbounded space

- **Central question:** Why is parity directly measurable even when photon number is unbounded?
- **Understanding target:** Interpret parity as even probability minus odd probability. Its measurement outcomes are always $+1$ or $-1$, so direct copies permit ordinary averaging. Distinguish the bounded target from the unbounded energy observable.
- **Dependencies and story role:** M01; isolates the quantity whose recovery will become difficult after loss.
- **Conceptual connection:** A simple observable can acquire a difficult statistical inverse through a noisy channel.
- **Sources:** L97 §2.2.2; [Recovery §1 and §6](../science/recovery.md).

### M03. Parity and the Wigner convention

- **Central question:** What does a negative parity say about the optical state?
- **Understanding target:** Use the project's convention $W_\rho(0)=2\theta/\pi$. Translate parity accuracy into Wigner-value accuracy, and distinguish a negative value at one point from a globally nonnegative Wigner function. Nonnegative origin parity alone establishes neither global positivity nor absence of negativity elsewhere.
- **Dependencies and story role:** M02; connects the observable to the certification question.
- **Conceptual connection:** A phase-space representation has an operational interpretation through a specified observable.
- **Sources:** L97 §3.1; [Model: photon counting and the generating function](../science/model.md).

### M04. What the loss channel removes

- **Central question:** Which information is unavailable after compulsory attenuation?
- **Understanding target:** Interpret pure loss as coupling to a vacuum environment through a beam splitter and discarding that environment. Known transmissivity specifies the channel; it does not supply lost-photon records or access to the source before loss.
- **Dependencies and story role:** M01; introduces the physical observation boundary.
- **Conceptual connection:** An open-system description determines the information available for inference.
- **Sources:** L97 §4.1.4; [Model: state, energy and channel](../science/model.md).

### M05. Binomial thinning of photon counts

- **Central question:** How does attenuation transform photon statistics?
- **Understanding target:** Explain why each input count produces a binomial received count, giving $q=T_\eta p$ and received mean at most $\eta E$. This count relation holds for coherent input states as well: the relevant output diagonal depends only on the input diagonal.
- **Dependencies and story role:** M01, M02, M04; reduces the measured part of the optical channel to an explicit stochastic map.
- **Conceptual connection:** Quantum loss contains a classical thinning experiment for this observable.
- **Sources:** L97 §§4.2.1, 5.2.2; [Model: photon counting](../science/model.md).

### M06. What a photon-tail promise guarantees

- **Central question:** What does a mean bound exclude, and what does it allow?
- **Understanding target:** For an integer cutoff $M\ge0$, use the tail bound $\Pr\{n>M\}\le E/(M+1)$ while recognizing that arbitrarily large counts remain possible. Separate a mean bound, a fixed higher moment, an exponential moment, and a hard support cutoff; these define different uniform state classes.
- **Dependencies and story role:** M01, M05; identifies the source information that controls difficulty.
- **Conceptual connection:** Rare high-photon events can respect an average budget while defeating stronger regularity assumptions.
- **Sources:** [Model](../science/model.md); [Interpretation: a rare component](../science/interpretation.md).

### M07. Accuracy, confidence, and the copy resource

- **Central question:** What must a successful procedure guarantee?
- **Understanding target:** Interpret additive error $\delta$, failure probability $\beta$, and a fixed copy budget uniformly over the allowed source class. Distinguish estimation from a promise test, whose intermediate states impose no requirement. Bias and nonlinear processing are allowed; every consumed copy counts.
- **Dependencies and story role:** M02, M03, M06; turns the physical question into a statistical task.
- **Conceptual connection:** A minimax guarantee concerns an entire promised class, rather than one chosen source.
- **Sources:** [Model: Tasks 1 and 2](../science/model.md).

### M08. Distinguishability and testing

- **Central question:** How does closeness of received distributions constrain a test?
- **Understanding target:** Distinguish $\ell^1$ distance, total variation, and directed chi-square divergence. Explain the connection between total variation and optimal binary testing error, and why processing data cannot increase distinguishability. Independent copies require a product-distribution calculation.
- **Dependencies and story role:** M05, M07; supplies the language for a converse.
- **Conceptual connection:** Observable separation before loss and statistical closeness after loss can force a copy lower bound.
- **Sources:** [Limits §§2–3](../science/limits.md); [bridge: research dependencies](LEONHARDT_BRIDGE.md).

### M09. Formal inversion and statistical stability

- **Central question:** Why does an inverse formula not settle recovery complexity?
- **Understanding target:** Recognize that inverse parity weights $(1-2/\eta)^k$ grow in magnitude under loss. A variance failure of this unbiased estimator leaves open biased or regularized procedures. Conversely, knowing the exact channel does not guarantee a stable inverse from finite data.
- **Dependencies and story role:** M02, M05, M07, M08; separates an established instability from the broader research question.
- **Conceptual connection:** Algebraic reconstruction and statistically useful inference require different guarantees.
- **Sources:** L97 §§5.3.1, 5.3.4; [Related work §1](../references/RELATED_WORK.md).

### M10. The geometry of generating functions

- **Central question:** Which part of the source generating function does the output reveal?
- **Understanding target:** Relate $P(-1)$ to parity and $Q(z)=P(1-\eta+\eta z)$ to loss. These are count-generating functions, distinct from phase-space $P,Q$ representations. The observed disk excludes $-1$ whenever $\eta<1$. Analytic uniqueness gives identifiability for positive transmissivity, while quantitative continuation determines stability.
- **Dependencies and story role:** M05, M06, M09; exposes the geometry behind the inverse problem.
- **Conceptual connection:** The location of a functional in the analytic domain changes its recoverability.
- **Sources:** [Recovery §2](../science/recovery.md); [Related work §3](../references/RELATED_WORK.md).

### M11. Moments as analytic regularity

- **Central question:** How does a photon moment constrain a generating function?
- **Understanding target:** For two mean-bounded laws, explain why their generating-function difference has a derivative uniformly bounded by $2E$, including continuous boundary values. Higher photon moments control higher derivatives; an exponential moment instead extends the analytic domain.
- **Dependencies and story role:** M06, M10; translates a physical promise into the regularity used by recovery.
- **Conceptual connection:** Tail information has a concrete derivative or analyticity meaning.
- **Sources:** [Recovery, R9–R13](../science/recovery.md); [Tail promises §2 and §6](../science/tail-promises.md).

### M12. Propagating bounds through an analytic domain

- **Central question:** How can information on one disk bound an unobserved value?
- **Understanding target:** Connect Cauchy estimates, subharmonic logarithms, the two-constants theorem, and harmonic measure. Understand the role of a Green-function barrier and distinguish continuation to a boundary point from continuation to an interior point.
- **Dependencies and story role:** M10, M11; supplies the analytic framework before the project-specific modulus calculation.
- **Conceptual connection:** Geometry weights how observed smallness competes with a global bound.
- **Sources:** [Recovery, R14–R20](../science/recovery.md); [Leonhardt bridge](LEONHARDT_BRIDGE.md).

### M13. The complete inference framework

- **Central question:** What must the two sides of a quantum minimax theorem cover?
- **Understanding target:** Assemble the known $E,\eta$, the unknown source, and the experiment with access only to received copies. A converse must cover every collective output POVM; a constructive upper may choose photon counting. Keep source accuracy $\delta$ separate from output-law tolerance $\epsilon$.
- **Dependencies and story role:** M01–M12; integrates the background into the precise problem.
- **Conceptual connection:** Physical access, statistical quantifiers, and analytic regularity jointly determine the claim.
- **Sources:** [Model](../science/model.md); [Scientific account](../science/README.md).

## Phase II: narrative and innovation — M14–M30

### M14. Different parity with matching moments

- **Central question:** How can two states differ in parity while matching many moments?
- **Understanding target:** Connect the binomial Fock mixture $b_m$ and its odd-conditioned counterpart $o_m$. Their generating-function difference has a zero of order $m$ at one, while their parities are zero and minus one. For $m\ge2$, both means are $m/2$.
- **Dependencies and story role:** M05, M10, M13; introduces the local hard mechanism.
- **Conceptual connection:** Moment agreement near one can coexist with a large boundary-parity difference.
- **Sources:** [Limits, L1–L6](../science/limits.md).

### M15. A globally Wigner-positive null

- **Central question:** What certifies positivity of the hard null throughout phase space?
- **Understanding target:** Explain the nonnegative closed Wigner expression for $b_m$, equivalently a half-attenuated number state. The baseline $b_1$ has mean one half and zero origin parity. Convex mixtures preserve global Wigner positivity, supplying more than an origin-only sign condition.
- **Dependencies and story role:** M03, M14; makes the hard pair suitable for the physical promise test.
- **Conceptual connection:** A tractable Fock mixture lies on the boundary of the Wigner-positive class.
- **Sources:** L97 §3.1; [Limits, L7 and L22–L23](../science/limits.md).

### M16. Rare components with many photons

- **Central question:** How can an increasingly large hard component fit a fixed mean budget?
- **Understanding target:** Track its weight $w$ and photon scale $m$: choosing $w$ proportional to $\delta$ permits $m$ proportional to $E/\delta$. Certification uses the available slack above energy one half. The worst-case family changes with the requested accuracy.
- **Dependencies and story role:** M06, M14, M15; embeds the local pair into the promised class.
- **Conceptual connection:** A small parity signal can carry a large conditional photon number without a large mean.
- **Sources:** [Limits §§4–5](../science/limits.md); [Interpretation](../science/interpretation.md).

### M17. The exact information remaining after loss

- **Central question:** How strongly does thinning hide this particular pair?
- **Understanding target:** Interpret the exact received chi-square divergence $(\eta/(2-\eta))^m$ and total variation $\eta^m/2$. Common-baseline dilution gives the chi-square upper bound with prefactor $w$. Distinguish these distances and their different roles in the copy analysis.
- **Dependencies and story role:** M08, M14, M16; quantifies the physical hiding mechanism.
- **Conceptual connection:** Binomial cancellation converts a high-photon parity contrast into exponentially weak received information.
- **Sources:** [Limits, L8–L14](../science/limits.md).

### M18. From a diagonal pair to an unrestricted converse

- **Central question:** Why can no collective quantum output measurement evade the pair?
- **Understanding target:** Express an arbitrary POVM on the diagonal product outputs as a stochastic kernel on photon-count strings. Combine data processing, chi-square tensorization, and midpoint testing to obtain the copy lower bound. This argument does not assume every optimal measurement is photon counting.
- **Dependencies and story role:** M08, M13, M17; turns the explicit pair into a quantum minimax obstruction.
- **Conceptual connection:** A commuting subfamily can constrain a much larger quantum decision problem.
- **Sources:** [Limits §3 and L21–L25](../science/limits.md).

### M19. Energy side information and endpoint qualifications

- **Central question:** Which qualifications are essential to interpreting the converse?
- **Understanding target:** Distinguish the vacuum case, the nonempty-alternative condition $E\ge(1+\delta)/2$, and the parametric lower bound from nearby two-level mixtures. Exact common-energy information does not defeat the adjusted hard pair. The recovery class still uses an inequality; exact-energy equality classes need not be compact.
- **Dependencies and story role:** M06, M15, M18; establishes the converse's valid budgets and endpoints.
- **Conceptual connection:** Side information and feasibility must be checked separately from the asymptotic mechanism.
- **Sources:** [Limits §§4–8](../science/limits.md).

### M20. Continuing the derivative

- **Central question:** How does the mean constraint bound the unobserved derivative?
- **Understanding target:** Combine the global derivative bound $2E$ with the observed-disk Cauchy bound $\epsilon/h$. Understand why shrinking the observed disk gives disjoint boundaries. The Green-function barrier lower-bounds harmonic measure by a constant times distance from $-1$ along the relevant real segment.
- **Dependencies and story role:** M11–M13; begins the constructive proof.
- **Conceptual connection:** The moment promise supplies precisely the regularity that continuation needs at the target boundary.
- **Sources:** [Recovery, R9–R20](../science/recovery.md).

### M21. The inverse-logarithmic modulus

- **Central question:** Why does integration produce the claimed accuracy dependence?
- **Understanding target:** Follow the integral of the continued derivative to the parity point. It gives a reciprocal logarithm of output tolerance, without an additional logarithm in the sample exponent. An exponentially small output error can therefore be sufficient for source error $\delta$.
- **Dependencies and story role:** M20; converts analytic continuation into a quantitative observable guarantee.
- **Conceptual connection:** Boundary regularity determines the modulus linking measured distributions to the desired functional.
- **Sources:** [Recovery, Theorem R1 and R21](../science/recovery.md).

### M22. A finite histogram for an infinite-support source

- **Central question:** How can the construction use finitely many measurement outcomes?
- **Understanding target:** Understand the theorem's cutoff $M=\lceil8E/\epsilon\rceil$, the overflow outcome, and the empirical $\ell^1$ confidence bound. Relocating the unknown input tail to vacuum proves existence of a finite fit while decreasing its mean; it is not an assumed physical source cutoff.
- **Dependencies and story role:** M05–M07, M21; turns the modulus into a finite statistical experiment.
- **Conceptual connection:** A uniform tail bound supports controlled approximation without unstable tail inversion.
- **Sources:** [Recovery, R22–R38](../science/recovery.md).

### M23. From a constrained fit to certification

- **Central question:** Why does every feasible fit give a valid parity estimate?
- **Understanding target:** Combine positivity, normalization, mean, and observed-distance constraints in the linear program. A fitted output has zero mass above the cutoff, so its full distance includes exactly the true overflow mass. Apply the modulus and account for coefficient precision; threshold the estimate only for the prescribed-origin promise.
- **Dependencies and story role:** M03, M15, M21, M22; completes the constructive statistical procedure.
- **Conceptual connection:** Confidence about received data becomes confidence about an unobserved source observable.
- **Sources:** [Recovery, R25–R43 and §7](../science/recovery.md).

### M24. The uniform loss crossover

- **Central question:** Which loss scales permit polynomial recovery?
- **Understanding target:** Join the bounds into $\log N=\Theta(\log(1/\delta)+\nu/\delta)$ with fixed $E>0$ for estimation, $E>1/2$ for certification, and a positive transmission floor. Distinguish the polynomial boundary $\nu=O(\delta\log(1/\delta))$ from uncorrected averaging: its bias is at most $2\nu E$, and $\nu E\le\delta/4$ suffices. The theorem matches logarithmic order, not exact exponential constants.
- **Dependencies and story role:** M18, M19, M23; integrates both proof directions into the main physical law.
- **Conceptual connection:** Regularized correction can remain useful after ignoring loss becomes inaccurate.
- **Sources:** [Model](../science/model.md); [Interpretation: two useful loss scales](../science/interpretation.md).

### M25. Higher derivatives from higher photon moments

- **Central question:** What analytic improvement does a fixed $s$-th moment supply?
- **Understanding target:** Replace the first derivative by the $s$-th derivative and use Taylor's integral remainder. Its kernel measures distance from the target endpoint, giving a reciprocal logarithm raised to power $s$. Keep the lower-order Taylor terms and the uniform choice of disk shrinkage in the error budget.
- **Dependencies and story role:** M11, M20, M21; identifies how the recovery mechanism changes under stronger promises.
- **Conceptual connection:** Each controlled derivative changes the inverse modulus quantitatively.
- **Sources:** [Tail promises §§2–3, especially T14](../science/tail-promises.md).

### M26. Matching the finite-moment hierarchy

- **Central question:** Can any fixed finite moment restore polynomial cost at fixed loss?
- **Understanding target:** Match the derivative upper with diluted pairs of photon scale proportional to $\delta^{-1/s}$. At fixed budget and fixed $s$, the loss term in $\log N$ is $\nu\delta^{-1/s}$; fixed loss still gives stretched exponential cost. The polynomial loss budget is $\nu=O(\delta^{1/s}\log(1/\delta))$. Certification requires moment budget above one half. Growing $s$ is outside this statement.
- **Dependencies and story role:** M16, M18, M24, M25; completes the stronger finite-moment comparison.
- **Conceptual connection:** Rare components survive every fixed finite-moment constraint, at a changed scale.
- **Sources:** [Tail promises, Theorem T1 and §5](../science/tail-promises.md).

### M27. Exponential tails and an interior target

- **Central question:** Why does an exponential photon moment permit polynomial recovery?
- **Understanding target:** Explain how $\operatorname{Tr}(R^{\hat n}\rho)\le B$, $R>1$, makes $-1$ interior to a larger analytic domain. The Hölder exponent gives a polynomial upper, not an optimal exponent; $R\ge4/\eta-3$ is sufficient for a parametric rate. Here $B=1$ permits only vacuum, and fixed-budget nontrivial certification requires $B>(1+R)/2$.
- **Dependencies and story role:** M09–M12, M25, M26; locates the boundary of the finite-moment conclusion.
- **Conceptual connection:** Enlarging an analytic domain changes the type of stability available.
- **Sources:** [Tail promises §§6–8](../science/tail-promises.md).

### M28. Proof, finite checks, and computational cost

- **Central question:** What does each kind of evidence or resource bound establish?
- **Understanding target:** Separate exact finite identities, floating-point optimization checks, and universal analytical proofs. The cutoff-32 examples are sensitivity illustrations. The theorem's detector cutoff, matrix size, arithmetic tolerance, and copy count are separate resources; finite LP construction does not imply efficient computation in inverse accuracy.
- **Dependencies and story role:** M22–M27; checks the operational meaning of the completed bounds.
- **Conceptual connection:** Information-theoretic achievability and numerical implementation have different obligations.
- **Sources:** [Verification](../verification/README.md); [Recovery §8](../science/recovery.md).

### M29. Inherited tools and the added conclusion

- **Central question:** What remains after established physics and inference methods receive credit?
- **Understanding target:** Attribute parity representations, thinning, unstable inverse weights, testing bounds, and continuation methods. Compare noisy-homodyne smoothness classes and direct-copy tomography with the present access and tail promises. Identify the added boundary-modulus calculation, physical positive-null hard family, matching order, and uniform loss crossover.
- **Dependencies and story role:** M18, M24, M26–M28; places the assembled result in its actual scientific context.
- **Conceptual connection:** A contribution is assessed through its model and conclusions, not merely shared terminology or methods.
- **Sources:** [Related work](../references/RELATED_WORK.md); [Bibliography](../references/REFERENCES.md); [Leonhardt bridge](LEONHARDT_BRIDGE.md).

### M30. What postloss data can certify

- **Central question:** What is the complete conclusion under a stated source promise?
- **Understanding target:** Explain the inverse-logarithmic worst-case precision at fixed positive loss, the lossless parametric rate, and the improvement from stronger tail information. State the known channel, access only after loss, and prescribed origin. Global positivity of the hard null strengthens the converse; accepting the null does not certify global positivity. No unknown-point search or universal difficulty for every fixed source family follows.
- **Dependencies and story role:** M13, M19, M24, M26–M29; integrates the entire scientific story.
- **Conceptual connection:** Rare photon events, analytic stability, and statistical distinguishability jointly set the power of an energy promise.
- **Sources:** [Model](../science/model.md); [Physical interpretation](../science/interpretation.md); [Scientific account](../science/README.md).
