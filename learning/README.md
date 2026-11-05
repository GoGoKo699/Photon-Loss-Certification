# Learning photon-loss certification

A photon counter reports how many photons arrive. Losing one photon changes an odd count into an even count, or an even count into an odd count. This makes the parity measured at the detector different from the parity of the source. The project asks how accurately source parity can be recovered when the loss is known but the source itself is unknown.

The central distinction is between a promise about the average photon number and a promise about the entire photon-number tail. A small average can coexist with rare, large photon numbers. Those rare events drive the worst-case precision law, even when collective quantum measurements are allowed.

## One anchor and a project-specific route

The educational anchor is **Ulf Leonhardt, *Measuring the Quantum State of Light* (1997)**. The [Leonhardt bridge](LEONHARDT_BRIDGE.md) identifies the relevant reading, fixes this project's conventions, and supplies the steps from optical state measurement to the statistical recovery problem. Its worked example makes the source-versus-detector distinction concrete.

The [30-milestone map](MILESTONES.md) organizes the project into two phases:

- **Background and preliminaries, M01–M13:** connect optical states, photon loss, parity, statistical distinguishability and the meaning of a uniform guarantee.
- **Narrative and innovation, M14–M30:** assemble the positive-null hard pair and the recovery construction, then connect their matching rates to the loss budget and stronger photon-tail promises.

Each milestone states an understanding target, dependencies, a conceptual connection and source pointers. The map follows the scientific argument; it does not require reading the whole book before approaching the result. Leonhardt supplies the optical foundation, while the repository supplies the additional statistical and analytic arguments.

## Choose a reading route

| Reader's question | Start here | Continue to |
|---|---|---|
| What changes when a photon is lost? | [Leonhardt bridge](LEONHARDT_BRIDGE.md) | [Physical interpretation](../science/interpretation.md) |
| How do the ideas connect from the beginning? | [Milestone map](MILESTONES.md) | The linked science at each milestone |
| What exactly is proved? | [Model and precision laws](../science/model.md) | [Limits](../science/limits.md) and [recovery](../science/recovery.md) |
| Which additional source promises improve recovery? | [Tail promises](../science/tail-promises.md) | Their lower constructions and finite estimators |
| How do the calculations and earlier work support the account? | [Verification guide](../verification/README.md) | [Related work](../references/RELATED_WORK.md) and [bibliography](../references/REFERENCES.md) |

The universal statements concern the source classes and access model in the scientific account. A finite example illustrates an operation or checks an identity; it does not replace a uniform proof. Throughout the route, keep source copies, detector resolution and computation as distinct resources.

[Repository overview](../README.md) · [Scientific account](../science/README.md)
