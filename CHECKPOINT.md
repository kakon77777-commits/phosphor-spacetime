# PHOSPHOR Spacetime Checkpoint — M0 + M1 + M2 + M3

- Version: `0.1.0a2`
- Date: 2026-08-23
- Repository: `kakon77777-commits/phosphor-spacetime`
- GitHub initialization: `9b73309edcdb87d89bc6d1902953aff6e2d93d75`
- Milestone 0 commit: `d5d7e02a930b5154682b688da57ddbfb482ddefa`
- Milestone 1 commit: `06e708c5379ab8607cc5b159919b82c727680ff8`
- Milestone 2 implementation commit: `10d5d70bb12ba47cdbc599c3da1d03b7937176fe`
- Milestone 3 implementation commit: `02ec2f2429b132dc687db1899774e84e8f2d264a`

## Implemented through M3

- Five canonical JSON contracts plus loader/validator.
- `TemporalState`, `DomainState`, `SpacetimeSnapshot`, `EvidenceRef`.
- Stable `DomainRegistry` and conflict-preserving `IRPatch` merge.
- `CommandIntent`, bounded `AuthorityGrant`, capability/bounds validation, fencing, idempotency, and provider-neutral `ActuationReceipt`.
- Deterministic Mock Provider with fail-closed unsupported/stale/exception/verification-mismatch paths.
- `ObservationEvent`, `ObserverBus`, and subscriber-failure isolation.
- `ProcessObserver` that samples only explicitly registered domain→PID mappings; no whole-machine scan fallback.
- Process CPU/RSS/VMS/status/create-time telemetry through `psutil`.
- `ObservationProjector` from observation events into derived Software Spacetime IR.
- Explicit `HEALTHY`, `STALE`, and `ERROR` observation semantics.
- Staleness refresh without requiring a new event.
- Observer error preserves the last good resource sample; later healthy recovery clears stale error metadata.

## Verification

Run from package root:

```bash
python -m pytest -q
```

Expected M3 checkpoint result: `31 passed`.

Additional verification:

```bash
python -m compileall -q src
python -m pip install -e . --no-deps --no-build-isolation -q
```

The local verification environment uses Python 3.13; the package contract remains Python `>=3.12`.

## Next

Milestone 4: Windows Job Object Provider — bounded real CPU/resource actuation for MVP-spawned or explicitly allowlisted test processes, with read-back verification and no semantic time-rate overclaim.
