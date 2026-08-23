# PHOSPHOR Spacetime Checkpoint — M0 + M1 + M2

- Version: `0.1.0a1`
- Date: 2026-08-23
- Repository: `kakon77777-commits/phosphor-spacetime`
- GitHub initialization: `9b73309edcdb87d89bc6d1902953aff6e2d93d75`
- Milestone 0 commit: `d5d7e02a930b5154682b688da57ddbfb482ddefa`
- Milestone 1 commit: `06e708c5379ab8607cc5b159919b82c727680ff8`
- Milestone 2 implementation commit: `10d5d70bb12ba47cdbc599c3da1d03b7937176fe`

## Implemented through M2

- Five canonical JSON contracts plus loader/validator.
- `TemporalState`, `DomainState`, `SpacetimeSnapshot`, `EvidenceRef`.
- Stable `DomainRegistry` and conflict-preserving `IRPatch` merge.
- `CommandIntent` and `ActorRef`.
- `AuthorityGrant` with target/action scope, expiry, and fencing epoch.
- Capability support/bounds validation.
- In-memory `IdempotencyStore` with terminal receipt reuse.
- Provider-neutral `ActuationReceipt`.
- Provider protocol and deterministic Mock Provider.
- Closed-loop dispatch: validate → authorize → apply → post-observe → verify.
- Fail-closed handling for unsupported capability, stale fence, expired intent, stale provider, provider exception, and post-observation mismatch.
- `PARTIAL` remains distinct from `CONFIRMED`.

## Verification

Run from package root:

```bash
python -m pytest -q
```

Expected M2 checkpoint result: `22 passed`.

Additional verification:

```bash
python -m compileall -q src
PYTHONPATH=src python -c "import phosphor_spacetime"
```

The local verification environment used Python 3.13; the package contract remains Python `>=3.12`.

## Next

Milestone 3: Observation Plane — observe only registered targets, add `ObserverBus`, `ProcessObserver`, projection updates, and stale-observation semantics.
