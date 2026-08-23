# PHOSPHOR Spacetime

**AI-native Software Spacetime Manager reference runtime.**

PHOSPHOR Spacetime explores a software control plane in which execution is represented as explicit **domains** with local temporal state, observation state, resource state, causal/governance references, and bounded actuation capabilities.

The project does **not** replace the kernel scheduler, PHOSPHOR, MCCP, CTCL, or HDUS. It integrates them through stable contracts:

```text
PHOSPHOR / MCCP / CTCL / OS / Runtime
                 ↓ evidence
         Software Spacetime IR
                 ↓
          Governance / Policy
                 ↓
            CommandIntent
                 ↓
           Authority Gate
                 ↓
            Actuation ABI
                 ↓
      HDUS / OS / Runtime Providers
                 ↓
           measured reality
```

## Status

`v0.1.0a6` — pre-alpha reference runtime.

Current implemented checkpoint:

- **Milestone 0 — Contracts:** complete.
- **Milestone 1 — Software Spacetime IR / Domain Registry:** complete.
- **Milestone 2 — Authority-Bounded Control Core + Mock Provider:** complete.
- **Milestone 3 — Registered Process Observation Plane:** complete.
- **Milestone 4 — Windows Job Object Provider:** complete.
- **Milestone 5 — Linux cgroup v2 Provider:** complete.
- **Milestone 6 — Synthetic Multi-Temporal Runtime:** complete.
- **Milestone 7 — Deterministic Rule Governor:** complete.
- Contracts include `ssm-ir-v0.1`, `ssm-control-v0.1`, `ssm-provider-v0.1`, `ssm-actuation-receipt-v0.1`, and `mvp-run-manifest-v0.1`.
- IR projection preserves observation conflicts rather than silently applying last-write-wins.
- M2 adds `CommandIntent`, bounded `AuthorityGrant`, capability/bounds validation, fencing, idempotency, `ActuationReceipt`, deterministic Mock Provider, and independent post-actuation verification.
- Provider exceptions, stale providers, unsupported capabilities, and verification mismatches fail closed rather than becoming false success.
- M3 adds `ObserverBus`, explicitly registered PID observation through `psutil`, stale-observation refresh, process-resource projection, subscriber-failure isolation, and error-to-healthy recovery semantics.
- Process observation never falls back to machine-wide discovery; unregistered PID/domain mappings return explicit observation errors.
- M4 adds a bounded Windows Job Object provider for MVP-spawned or explicitly allowlisted processes, with CPU hard-cap and job-memory policy read-back.
- Windows process pause/resume is explicitly `PARTIAL` process-level control; generic `domain.set_temporal_rate` remains `UNSUPPORTED` because `CPUServiceRate != LogicalTimeRate`.
- Native Windows CI evidence: workflow run `32641297667`, job `97198681707`, Windows Server 2025 / Python 3.12.10, `PSS_RUN_WINDOWS_JOB_TESTS=1`, **39 passed**.
- M5 adds a dedicated-subtree Linux cgroup v2 provider with separate `cpu.weight` / `cpu.max`, `memory.max`, `io.weight` / `io.max`, cgroup freeze, read-back verification, and fail-closed unknown-resource handling.
- Generic Linux `domain.set_temporal_rate` remains `UNSUPPORTED`; cgroup CPU service controls are not logical-time controls.
- Native Linux CI evidence: workflow run `32643114760`, Ubuntu job `97203159145`, Ubuntu 24.04 / Python 3.12.14, `PSS_RUN_CGROUP_TESTS=1`, **49 passed / 1 Windows-only skip**.
- The same run's Windows job `97203159312` remained green with **49 passed / 1 Linux-only skip**.
- M6 adds a deterministic Synthetic Runtime with native logical clock, requested/realized rate, fractional rate remainder, pause/resume, discrete event queue, event-jump execution, snapshot/restore, deterministic PRNG state, and canonical state hash.
- Tick execution and event-jump execution can perform different amounts of work while producing the same semantic state hash; the reference event-sparse workload reaches tick 1000 with `1000` tick iterations in tick mode and `0` tick iterations in event-jump mode.
- Synthetic `domain.set_temporal_rate` is `SUPPORTED` as `LOGICAL_RATE_NATIVE`, creating a ground-truth contrast with M4/M5 OS resource-service controls.
- M6 CI evidence: workflow run `32644861647`; Ubuntu job `97207461111` and Windows job `97207461220` both passed with **62 passed / 1 opposite-platform native skip**.
- M7 adds provider-neutral `GovernanceSummary` / `PolicyProposal` and a deterministic Rule Governor over temporal debt, resource pressure, causal criticality, and observation health.
- M7 enforces hysteresis bands, cooldown, per-decision max-delta bounds, native logical-rate preference, CPU-budget fallback, background pressure relief, bounded pause/resume, and observation-profile adaptation.
- Stale/error observations produce no adaptive mutation; policy proposals remain untrusted governance intents and never gain provider authority.
- M7 CI evidence: workflow run `32645942343`; Ubuntu job `97210098401` and Windows job `97210098521` both passed with **78 passed / 1 opposite-platform native skip**.

Run verification:

```bash
python -m pytest -q
```

## Core invariants

- `Time != Compute`
- `Observation != Authority`
- `Causality != Containment`
- `CommandIntent != Actuation`
- `Desired != Requested != Realized != Observed`
- `HDUS != HyperSoul`
- `UI != CanonicalSource`
- Unsupported or ambiguous mutation fails closed.
- Observation failure must not crash the target workload.

## Architecture documents

See [`docs/architecture/README.md`](docs/architecture/README.md).

The pre-MVP series contains four theory papers and three engineering whitepapers. The repository starts implementation from the three engineering documents:

1. PHOSPHOR Spacetime Architecture v0.1
2. HDUS Virtual Actuation Plane v0.1
3. PHOSPHOR Spacetime MVP v0.1

## Related repositories

- [eml-phosphor](https://github.com/kakon77777-commits/eml-phosphor) — execution-as-interface, CTS, AI-readable event stream.
- [phosphor-mccp](https://github.com/kakon77777-commits/phosphor-mccp) — runtime tracing, computational graph, evidence-grounded analysis.

CTCL and HDUS remain independent canonical systems and are connected through adapters rather than copied into this repository.

## MVP policy

This repository is intentionally **local-first** and **userspace-first**. Initial actuation is limited to workloads spawned by the MVP or explicitly allowlisted test targets. Closed-source games are not used as foundational correctness oracles; synthetic and instrumented runtimes come first.

## License

Apache-2.0.
