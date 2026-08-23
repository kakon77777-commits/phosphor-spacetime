# PHOSPHOR Spacetime Checkpoint — M0 through M7

- Version: `0.1.0a6`
- Date: 2026-08-23
- Repository: `kakon77777-commits/phosphor-spacetime`
- M6 closure: `358b9024a06ff5f24682ef1c4d74dd416117cd9f`
- M7 feature merge: `4d90cb6cfc985ecf6edcc895a2c9e159e69b01f4`

## Implemented through M7

- Contracts, IR, Domain Registry, observation, authority-bound control, receipts, Windows Job Object, Linux cgroup v2, and Synthetic Runtime remain intact.
- Provider-neutral `GovernanceSummary` and `PolicyProposal`.
- Deterministic Rule Governor inputs: temporal debt, normalized resource pressure, causal criticality, observation health, current temporal/resource state, and capability availability.
- Hysteresis uses separate low/high thresholds; cooldown blocks rapid repeated changes.
- CPU and temporal adjustments are bounded by both configured step and hard `max_delta`.
- High critical debt prefers native logical-time control; CPU budget is only a fallback, preserving `Time != Compute`.
- Low-criticality background work under pressure is throttled before pause; critical paused work with debt can resume.
- Stale/error observation blocks adaptive mutation.
- Observation adaptation never downgrades an existing `FORENSIC` profile to `FOCUSED`.
- M7 emits proposals only; authority validation and provider dispatch remain separate layers.

## M7 Correctness Evidence

- Local Governor tests: `16 passed`.
- Full local regression before closure: `77 passed, 2 skipped` (two platform-native tests).
- Regression caught and fixed an observation-policy direction bug: `FORENSIC -> FOCUSED` downgrade is now forbidden.
- Native temporal rate at ceiling falls back to resource proposal instead of pretending time can exceed its capability bound.

## CI Evidence

Workflow run `32645942343`:
- Ubuntu job `97210098401`: `78 passed, 1 skipped`; Linux cgroup native path executed.
- Windows job `97210098521`: `78 passed, 1 skipped`; Windows Job Object native path executed.

## Next

M8 AI Policy Adapter: structured summary input, schema-bounded PolicyProposal output, timeout/malformed-output failure handling, and deterministic Rule Governor fallback.
