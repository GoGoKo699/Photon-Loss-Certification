# References

The source comparisons are in [Related work](RELATED_WORK.md). Citation keys below are stable links for the mathematical notes. Published versions are identified separately from preprints when the distinction affects a claim.

## Photon counting, Wigner functions, and inverse estimation

### Royer77

Antoine Royer, **Wigner function as the expectation value of a parity operator**, *Physical Review A* **15**, 449–450 (1977). [Publisher and DOI](https://doi.org/10.1103/PhysRevA.15.449).

The displaced-parity interpretation of the Wigner function. Numerical prefactors depend on phase-space conventions; this repository uses $W_\rho(0)=(2/\pi)\operatorname{Tr}[(-1)^{\hat n}\rho]$.

### Ban99

Konrad Banaszek, **Statistical uncertainty in quantum optical photodetection measurements**, *Journal of Modern Optics* **46**, 675–692 (1999). [Preprint, arXiv:quant-ph/9801059v2](https://arxiv.org/abs/quant-ph/9801059v2) (23 March 1998).

Section III, especially Eqs. (20)–(22), analyzes inverse-loss parity weights and their statistical instability. The journal year is 1999; the cited preprint version is from 1998.

### BGA07

Cristina Butucea, Mădălin Guţă, and Luis Artiles, **Minimax and adaptive estimation of the Wigner function in quantum homodyne tomography with noisy data**, *The Annals of Statistics* **35**(2), 465–494 (2007). [DOI](https://doi.org/10.1214/009053606000001488); [preprint, arXiv:math/0504058v3](https://arxiv.org/abs/math/0504058v3).

Pointwise Wigner minimax estimation from inefficient homodyne data over fixed exponentially weighted Fourier classes. See Section 3 for the classes and Theorem 1 for the rates.

### WLPG11

Jinlong Wu, Tiejun Li, Xiang Peng, and Hong Guo, **Statistical method for resolving the photon–photoelectron-counting inversion problem**, *Journal of Computational Physics* **230**(3), 726–743 (2011). [DOI](https://doi.org/10.1016/j.jcp.2010.10.015); [publisher abstract and introduction](https://www.sciencedirect.com/science/article/abs/pii/S0021999110005693).

Binomial-mixture inversion, ill-posedness, and a Bayesian coarse-graining approach. **Access boundary:** the comparison here uses the publisher's accessible abstract and introduction. The full article was not available for inspection, so no conclusion about an uninspected theorem is asserted.

### PSW17

Yury Polyanskiy, Ananda Theertha Suresh, and Yihong Wu, **Sample complexity of population recovery**, *Proceedings of the 30th Conference on Learning Theory*, PMLR **65**, 1589–1618 (2017). [Proceedings page](https://proceedings.mlr.press/v65/polyanskiy17a.html); [full paper](https://proceedings.mlr.press/v65/polyanskiy17a/polyanskiy17a.pdf).

Theorem 4 gives a linear-functional mixture-estimation framework through linear-program duality and two-point lower bounds. Section 3 and Proposition 9 use probability generating functions and complex analysis for lossy coordinate recovery.

### Tre20

Lloyd N. Trefethen, **Quantifying the ill-conditioning of analytic continuation**, *BIT Numerical Mathematics* **60**, 901–915 (2020). [DOI](https://doi.org/10.1007/s10543-020-00802-7); [author's institutional record](https://ora.ox.ac.uk/objects/uuid%3A0e4de186-e63c-4ec3-bc1c-4b6af4fe012b).

Background on quantitative analytic continuation under a boundedness promise. The maximum principle, two-constants argument, and harmonic-measure method used in this repository are classical tools.

## Quantum learning, mitigation, and certification

### CRW21

Ulysse Chabaud, Ganaël Roeland, Mattia Walschaers, Frédéric Grosshans, Valentina Parigi, Damian Markham, and Nicolas Treps, **Certification of Non-Gaussian States with Operational Measurements**, *PRX Quantum* **2**, 020333 (2021). [DOI](https://doi.org/10.1103/PRXQuantum.2.020333); [preprint, arXiv:2011.04320](https://arxiv.org/abs/2011.04320).

Operational certification with finite Fock-space observables and double-homodyne data; Section IV gives truncated odd-photon witnesses of Wigner negativity.

### CEG21

Ulysse Chabaud, Pierre-Emmanuel Emeriau, and Frédéric Grosshans, **Witnessing Wigner Negativity**, *Quantum* **5**, 471 (2021). [Published article](https://quantum-journal.org/papers/q-2021-06-08-471/); [DOI](https://doi.org/10.22331/q-2021-06-08-471); [updated preprint, arXiv:2102.06193v6](https://arxiv.org/abs/2102.06193v6).

Complete families of witnesses and optimization of their thresholds over Wigner-positive states. The updated preprint contains corrections and additional optimization details; it is identified explicitly rather than treated as identical to every earlier version.

### TTG23

Ryuji Takagi, Hiroyasu Tajima, and Mile Gu, **Universal Sampling Lower Bounds for Quantum Error Mitigation**, *Physical Review Letters* **131**, 210602 (2023). [DOI](https://doi.org/10.1103/PhysRevLett.131.210602); [preprint, arXiv:2208.09178v4](https://arxiv.org/abs/2208.09178v4).

Theorem 1 lower-bounds general mitigation procedures using the distinguishability of noisy state pairs. It supplies the general information-theoretic principle behind the converse here.

### TBKK24

Adam Taylor, Gabriele Bressanini, Hyukjoon Kwon, and M. S. Kim, **Quantum error cancellation in photonic systems: Undoing photon losses**, *Physical Review A* **110**, 022622 (2024). [DOI](https://doi.org/10.1103/PhysRevA.110.022622); [preprint, arXiv:2403.05252v2](https://arxiv.org/abs/2403.05252v2) (28 June 2024).

Inverse-channel error cancellation using noiseless amplification, photon subtraction, and signed sampling; includes source-dependent alternatives and explicit overhead analyses.

### Mele25

Francesco A. Mele, Antonio A. Mele, Lennart Bittel, Jens Eisert, Vittorio Giovannetti, Ludovico Lami, Lorenzo Leone, and Salvatore F. E. Oliviero, **Learning quantum states of continuous-variable systems**, *Nature Physics* **21**, 2002–2008 (2025). [Published article and DOI](https://doi.org/10.1038/s41567-025-03086-2); [open published text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12695625/); [preprint, arXiv:2405.01431v4](https://arxiv.org/abs/2405.01431v4).

Sample complexity of learning continuous-variable states from direct copies under energy and higher-moment constraints. This is the direct-access benchmark for the compulsory-loss setting studied here.

### FOS26

Omar Fawzi, Aadil Oufkir, and Robert Salzmann, **Optimal Fidelity Estimation from Binary Measurements for Discrete and Continuous Variable Systems**, *PRX Quantum* **7**, 010309 (2026). [Published article and DOI](https://doi.org/10.1103/qd1c-1fk9); [publisher PDF](https://journals.aps.org/prxquantum/pdf/10.1103/qd1c-1fk9); [preprint, arXiv:2409.04189v1](https://arxiv.org/abs/2409.04189v1).

The main task is fidelity estimation from binary measurements. **Version distinction:** published Appendix B treats photon-loss robustness under an energy constraint; this appendix is absent from the inspected arXiv v1. Claims about that appendix refer to the published paper.

## Background texts

These books provide entry points to the optical and quantum-information formalism. They are not cited as sources of the minimax rate proved in this repository.

### Leo97

Ulf Leonhardt, **Measuring the Quantum State of Light**, Cambridge Studies in Modern Optics **22**, Cambridge University Press (1997), ISBN 9780521497305. [Publisher front matter](https://assets.cambridge.org/97805214/97305/frontmatter/9780521497305_frontmatter.pdf); [author's institutional bibliographic record](https://research-portal.st-andrews.ac.uk/en/publications/measuring-the-quantum-state-of-light/).

Background on optical quantum-state measurement and phase-space representations.

### Hol19

Alexander S. Holevo, **Quantum Systems, Channels, Information: A Mathematical Introduction**, second revised and expanded edition, De Gruyter (2019). [Publisher and DOI](https://doi.org/10.1515/9783110642490).

Part V, especially Chapters 11–12, treats constrained inputs and Gaussian systems in infinite-dimensional quantum information.

### Wat18

John Watrous, **The Theory of Quantum Information**, Cambridge University Press (2018). [Publisher and DOI](https://doi.org/10.1017/9781316848142); [author's page with manuscript and errata](https://cs.uwaterloo.ca/~watrous/TQI/).

Chapters 2–3 provide the states, channels, measurements, and distinguishability background used in the finite-support lower-bound construction. Infinite-dimensional channel conventions are covered by Hol19.
