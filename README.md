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

`v0.1.0a2` — pre-alpha reference runtime.

Current implemented checkpoint:

- **Milestone 0 — Contracts:** complete.
- **Milestone 1 — Software Spacetime IR / Domain Registry:** complete.
- **Milestone 2 — Authority-Bounded Control Core + Mock Provider:** complete.
- **Milestone 3 — Registered Process Observation Plane:** complete.
- Contracts include `ssm-ir-v0.1`, `ssm-control-v0.1`, `ssm-provider-v0.1`, `ssm-actuation-receipt-v0.1`, and `mvp-run-manifest-v0.1`.
- IR projection preserves observation conflicts rather than silently applying last-write-wins.
- M2 adds `CommandIntent`, bounded `AuthorityGrant`, capability/bounds validation, fencing, idempotency, `ActuationReceipt`, deterministic Mock Provider, and independent post-actuation verification.
- Provider exceptions, stale providers, unsupported capabilities, and verification mismatches fail closed rather than becoming false success.
- M3 adds `ObserverBus`, explicitly registered PID observation through `psutil`, stale-observation refresh, process-resource projection, subscriber-failure isolation, and error-to-healthy recovery semantics.
- Process observation never falls back to machine-wide discovery; unregistered PID/domain mappings return explicit observation errors.

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
