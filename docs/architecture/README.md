# PHOSPHOR Spacetime Architecture Documents

This repository implements the engineering closure of a seven-document pre-MVP series.

## Theory foundation

1. **Software Spacetime** — domains, local time, observers, worldlines, branch/replay.
2. **Multi-Temporal Computing** — requested/realized temporal rates, temporal debt, synchronization boundaries.
3. **Software Causal Topology** — work, depth, structural parallelism, poset width, scheduler/SSM separation.
4. **Fractal AI Spacetime Governance** — global/local governance, capability/authority, escalation and failure containment.

## Engineering contracts

5. [`PHOSPHOR_SPACETIME_ARCHITECTURE_v0.1.md`](PHOSPHOR_SPACETIME_ARCHITECTURE_v0.1.md) — six-plane integration architecture and Software Spacetime IR.
6. [`HDUS_VIRTUAL_ACTUATION_PLANE_v0.1.md`](HDUS_VIRTUAL_ACTUATION_PLANE_v0.1.md) — provider-neutral actuation contract and Pre-HyperSoul simulation layer.
7. [`PHOSPHOR_SPACETIME_MVP_v0.1.md`](PHOSPHOR_SPACETIME_MVP_v0.1.md) — implementation, workloads, baselines, gates, and falsification criteria.

## Implementation rule

No new pre-MVP theory paper is required before the reference runtime. The next canonical loop is:

```text
Implement → Measure → Break → Revise
```

## Current implementation checkpoint

- M0 Contracts: complete.
- M1 Software Spacetime IR / Domain Registry: complete.
- M2 Authority-Bounded Control Core + Mock Provider: complete.
- M3 Registered Process Observation Plane: complete.
- M4 Windows Job Object Provider: complete.
- M5 Linux cgroup v2 Provider: complete.
- M6 Synthetic Multi-Temporal Runtime: complete.
- Next: M7 Deterministic Rule Governor — bounded temporal/resource policy with hysteresis and cooldown.

M2 main implementation commit: `10d5d70bb12ba47cdbc599c3da1d03b7937176fe`.
M3 main implementation commit: `02ec2f2429b132dc687db1899774e84e8f2d264a`.
M4 main implementation commit: `9452b49d8dcd5b85dfbcafea50f80cb621b92228`.
M4 validation merge commit: `295cd933a6f14321b650b2bdf9c4f19ded40df1b`.
M4 native Windows validation: workflow run `32641297667`, Windows job `97198681707`, `39 passed`.

M5 implementation commit: `23764e1ebaf1231a9e40dc5539d72436511825c3`.
M5 validation merge: `99417eaa8d069c55a1c3ef541b7254b340095af6`.
M5 native Linux validation: workflow `32643114760`, Ubuntu job `97203159145`, `49 passed / 1 Windows-only skip`.

M6 feature merge: `56b678e2868c17f44d7ccdb037140b58677b091e`.
M6 validation: workflow `32644861647`; Ubuntu `97207461111` and Windows `97207461220`, both `62 passed / 1 opposite-platform native skip`.
