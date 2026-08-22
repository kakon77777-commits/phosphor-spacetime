# PHOSPHOR Spacetime Architecture

This repository implements the engineering closure of a seven-document pre-MVP series.

## Theory foundation

1. **Software Spacetime** — domains, local time, observers, worldlines, branch/replay.
2. **Multi-Temporal Computing** — requested/realized temporal rates, temporal debt, synchronization boundaries.
3. **Software Causal Topology** — work, depth, structural parallelism, poset width, scheduler/SSM separation.
4. **Fractal AI Spacetime Governance** — global/local governance, capability/authority, escalation and failure containment.

## Engineering contracts

5. **PHOSPHOR Spacetime Architecture v0.1** — six-plane integration architecture and Software Spacetime IR.
6. **HDUS Virtual Actuation Plane v0.1** — provider-neutral actuation contract and Pre-HyperSoul simulation layer.
7. **PHOSPHOR Spacetime MVP v0.1** — implementation, workloads, baselines, gates, and falsification criteria.

The canonical source packs are preserved separately; the executable contracts live under `schemas/` and are implemented incrementally in `src/phosphor_spacetime/`.

## Current implementation

- M0 Contracts: complete.
- M1 IR / Domain Registry: complete.
- Next: M2 Control Core — CommandIntent, Authority Gate, Fencing, Idempotency, and ActuationReceipt.

## Rule

No new pre-MVP theory paper is required before the reference runtime. The engineering loop is:

```text
Implement → Measure → Break → Revise
```
