# PHOSPHOR Spacetime Checkpoint — M0 through M6

- Version: `0.1.0a5`
- Date: 2026-08-23
- Repository: `kakon77777-commits/phosphor-spacetime`
- M5 closure: `5b335811bbc5813c5112594c2e7d7e9e4c9420b9`
- M6 feature merge: `56b678e2868c17f44d7ccdb037140b58677b091e`

## Implemented through M6

- Contracts, Software Spacetime IR, Domain Registry, conflict-preserving projection.
- Authority-bounded CommandIntent, fencing, idempotency, receipts, Mock Provider.
- Registered process Observation Plane.
- Native Windows Job Object Provider and Linux cgroup v2 Provider with read-back verification.
- Deterministic Synthetic Runtime as the first native logical-time ground-truth provider.
- Synthetic runtime supports logical tick, requested/realized logical rate, fractional rate remainder, pause/resume, discrete event queue, tick execution, exact event-jump execution, snapshot/restore, deterministic PRNG state, and canonical state hash.
- Snapshot preserves pending events, rate remainder, PRNG state, and future event ordering; restore recreates the same future trajectory.
- Event payloads must be canonical JSON-serializable data with finite numeric values.
- Synthetic `domain.set_temporal_rate` is native logical-time control; Windows/Linux CPU resource controls remain explicitly separate.

## M6 Correctness Evidence

- Same seed + same schedule -> same state hash.
- Different seed affects random events and state hash.
- Tick and event-jump modes produce the same final semantic hash at equal logical time.
- Reference event-sparse workload at tick `1000`: tick mode uses `1000` tick iterations; event-jump mode uses `0` tick iterations while producing the same final state hash.
- Snapshot/restore reproduces future execution exactly, including deterministic random events.
- Provider snapshot/restore and native rate controls pass the existing authority / receipt / post-observation verification path.

## CI Evidence

Workflow run `32644861647`:
- Ubuntu job `97207461111`: `62 passed, 1 skipped` (Windows-only native test skipped); Linux cgroup native path executed.
- Windows job `97207461220`: `62 passed, 1 skipped` (Linux-only native test skipped); Windows Job Object native path executed.

## Next

M7 Deterministic Rule Governor: temporal debt, resource pressure, causal criticality, observation health, hysteresis, cooldown, and bounded policy proposals.
