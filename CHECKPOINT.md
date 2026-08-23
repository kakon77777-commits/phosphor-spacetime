# PHOSPHOR Spacetime Checkpoint — M0 through M8

- Version: `0.1.0a7`
- Date: 2026-08-23
- Repository: `kakon77777-commits/phosphor-spacetime`
- M7 closure head: `da65ee2d7faa98cd059f545c34eab5e56e63267c`
- M8 feature merge: `7511a73b635f0b845759fe9097cbb4b4a7234aa8`

## Implemented through M8

- M0–M7 contracts, IR, observation, authority, providers, Synthetic Runtime, and deterministic Rule Governor remain intact.
- `AIPolicyAdapter` consumes only compact provider-neutral `GovernanceSummary` input.
- AI output is a strict single-proposal envelope with target domain, operation, value, goal, reason, confidence, and evidence references.
- Provider-specific raw commands, cross-domain targets, invented evidence, unsupported operations, strict-type violations, and out-of-envelope rate/budget changes are rejected.
- AI evidence `(source,id)` references are rebound to canonical `EvidenceRef` objects from the current summary.
- AI timeout, malformed JSON, schema rejection, model exception, and contained non-`Exception` BaseException paths all fail over to the M7 Rule Governor.
- Stale/error observation and active policy cooldown block the AI call before model budget is spent.
- AI proposals never carry provider or actuation authority; `PolicyProposal != CommandIntent != Actuation`.
- AI pause is restricted to low-criticality background domains; observation down-resolution is restricted to quiet low-criticality background domains and never downgrades `FORENSIC`.

## M8 Correctness Evidence

- Local M8 targeted tests: `23 passed`.
- Full local regression before closure: `100 passed, 2 skipped` (two platform-native tests).
- TDD caught a Pydantic exception-hierarchy classification bug: `ValidationError` must be classified as `REJECTED`, not malformed output.
- Adversarial tests cover timeout, malformed JSON, raw provider commands, target mismatch, invented evidence, bounds/delta violations, stale/cooldown blocking, explicit abstain, observation downgrade, and BaseException containment.

## CI Evidence

Workflow run `32647644223`:
- Ubuntu job `97214257354`: `101 passed, 1 skipped`; Linux cgroup v2 native path executed.
- Windows job `97214257243`: `101 passed, 1 skipped`; Windows Job Object native path executed.

## Next

M9 Benchmark Harness / baseline closure: formal B0 Native, B1 Fixed, B2 Rule, and B3 AI-assisted runs with manifests, correctness contracts, metrics, and comparison artifacts.
