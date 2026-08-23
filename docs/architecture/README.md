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

```text
Implement → Measure → Break → Revise
```

No additional pre-MVP theory paper is required before runtime evidence.

## Runtime checkpoints

- M0 Contracts: complete.
- M1 Software Spacetime IR / Domain Registry: complete.
- M2 Authority-Bounded Control Core + Mock Provider: complete.
- M3 Registered Process Observation Plane: complete.
- M4 Windows Job Object Provider: complete.
- M5 Linux cgroup v2 Provider: complete.
- M6 Synthetic Multi-Temporal Runtime: complete.
- M7 Deterministic Rule Governor: complete.
- M8 Schema-Bounded AI Policy Adapter: complete.
- M9 Benchmark Harness / B0–B3 Baseline Closure: complete.
- Next: M10 Gate Runner + Failure Injection.

## Governance and actuation boundary

```text
Observation
  ↓
Software Spacetime IR
  ↓
GovernanceSummary
  ├─→ Rule Governor ─┐
  └─→ AI Adapter ────┤ PolicyProposal
                     ↓
                deterministic validation
                     ↓
                 CommandIntent
                     ↓
                Authority Gate
                     ↓
                 Provider ABI
                     ↓
                measured reality
```

`PolicyProposal != CommandIntent != Actuation`. AI never receives provider authority.

## M9 benchmark architecture

M9 introduces a reproducible evidence layer:

```text
Workload + Seed + Baseline + Commit
                ↓
            Run Manifest
                ↓
     B0 / B1 / B2 / B3 Policy
                ↓
         Workload Execution
                ↓
 Correctness + Metrics + Artifacts
                ↓
       Compatibility-Aware Compare
```

The baseline contract is:

- `B0_NATIVE`: native/default execution, no adaptive policy.
- `B1_FIXED`: explicit fixed policy, no runtime adaptation.
- `B2_RULE`: deterministic Rule Governor.
- `B3_AI`: M8 schema-bounded AI adapter with deterministic Rule fallback.

M9 does not encode `B2 > B1` or `B3 > B2` as hard gates. The harness first establishes fair, reproducible, correctness-preserving measurement. Performance superiority is tested later through repeated formal runs.

M9 feature merge: `773a23e4a846e3e944691a278569cd07e74ed3b8`.
M9 validation workflow: `32649039908`; Ubuntu `97217661925` and Windows `97217662030`, both `117 passed / 1 opposite-platform native skip`.

## Next architectural checkpoint

M10 will encode Gate 0–6 and failure injection: observer crash, provider stale state, receipt mismatch, AI timeout/error, duplicate command, and stale fencing. Hard gates remain distinct from tunable performance hypotheses.
