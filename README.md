# PHOSPHOR Spacetime

**AI-native Software Spacetime Manager reference runtime.**

PHOSPHOR Spacetime represents execution as explicit software-spacetime domains with local temporal state, observation state, resource state, governance state, and bounded actuation capabilities. It integrates PHOSPHOR, MCCP, CTCL, HDUS, operating-system controls, and instrumented runtimes through adapters rather than replacing their canonical source schemas.

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

`v0.1.0a8` — pre-alpha reference runtime.

Implemented checkpoints:

- **M0** Contracts
- **M1** Software Spacetime IR / Domain Registry
- **M2** Authority-Bounded Control Core + Mock Provider
- **M3** Registered Process Observation Plane
- **M4** Windows Job Object Provider
- **M5** Linux cgroup v2 Provider
- **M6** Synthetic Multi-Temporal Runtime
- **M7** Deterministic Rule Governor
- **M8** Schema-Bounded AI Policy Adapter
- **M9** Benchmark Harness / B0–B3 Baseline Closure

M9 adds reproducible run manifests, correctness-preserving A–E synthetic workloads, B0 Native / B1 Fixed / B2 Rule / B3 AI orchestration, invalid-run retention, comparison integrity warnings, numeric aggregation, and the installable `pss` CLI.

```bash
pss run C_EVENT_SPARSE --baseline B0_NATIVE
pss matrix C_EVENT_SPARSE
pss compare runs/<run-a> runs/<run-b>
```

M9 intentionally does **not** make `B2 > B1` or `B3 > B2` a hard pass condition. Performance superiority remains an empirical hypothesis for repeated benchmark runs.

## Core invariants

- `Time != Compute`
- `Observation != Authority`
- `Capability != Authority`
- `Causality != Containment`
- `CommandIntent != Actuation`
- `PolicyProposal != CommandIntent`
- `Desired != Requested != Realized != Observed`
- `CPUServiceRate != LogicalTimeRate`
- `HDUS != HyperSoul`
- `UI != CanonicalSource`
- Unsupported or ambiguous mutation fails closed.
- Observation failure must not crash the target workload.
- AI failure must not imply governance or host failure.

## Benchmark baselines

- `B0_NATIVE` — native/default execution, no adaptive policy.
- `B1_FIXED` — fixed policy, no runtime adaptation.
- `B2_RULE` — deterministic Rule Governor.
- `B3_AI` — M8 schema-bounded AI policy with deterministic Rule fallback.

Formal run artifacts include `manifest.json`, `config.json`, `metrics.json`, `correctness.json`, `command-intents.jsonl`, `actuation-receipts.jsonl`, and `summary.md`. Failed runs are retained as invalid evidence instead of silently discarded.

## Verification

```bash
python -m pytest -q
```

M9 PR validation run `32649039908` completed with:

- Ubuntu job `97217661925`: **117 passed / 1 Windows-only skip**, native Linux cgroup v2 path executed.
- Windows job `97217662030`: **117 passed / 1 Linux-only skip**, native Windows Job Object path executed.

See [`CHECKPOINT.md`](CHECKPOINT.md) for milestone evidence and [`docs/architecture/README.md`](docs/architecture/README.md) for architecture history.

## Related repositories

- [eml-phosphor](https://github.com/kakon77777-commits/eml-phosphor)
- [phosphor-mccp](https://github.com/kakon77777-commits/phosphor-mccp)

CTCL and HDUS remain independent canonical systems and are connected through adapters rather than copied into this repository.

## MVP policy

The runtime is intentionally **local-first** and **userspace-first**. Initial actuation is limited to workloads spawned by the MVP or explicitly allowlisted test targets. Synthetic and instrumented runtimes are used as foundational correctness oracles before closed-source targets.

## License

Apache-2.0.
