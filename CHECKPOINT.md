# PHOSPHOR Spacetime Checkpoint — M0 + M1 + M2 + M3 + M4

- Version: `0.1.0a3`
- Date: 2026-08-23
- Repository: `kakon77777-commits/phosphor-spacetime`
- GitHub initialization: `9b73309edcdb87d89bc6d1902953aff6e2d93d75`
- Milestone 0 commit: `d5d7e02a930b5154682b688da57ddbfb482ddefa`
- Milestone 1 commit: `06e708c5379ab8607cc5b159919b82c727680ff8`
- Milestone 2 implementation commit: `10d5d70bb12ba47cdbc599c3da1d03b7937176fe`
- Milestone 3 implementation commit: `02ec2f2429b132dc687db1899774e84e8f2d264a`
- Milestone 4 implementation commit: `9452b49d8dcd5b85dfbcafea50f80cb621b92228`
- Milestone 4 validation merge: `295cd933a6f14321b650b2bdf9c4f19ded40df1b`

## Implemented through M4

- Five canonical JSON contracts plus loader/validator.
- Software Spacetime IR, stable Domain Registry, and conflict-preserving projection.
- Authority-bounded CommandIntent, fencing, idempotency, provider-neutral receipts, and independent post-actuation verification.
- Registered-process Observation Plane with explicit HEALTHY / STALE / ERROR semantics.
- Windows Job Object Provider for MVP-spawned or explicitly allowlisted test targets.
- CPU hard-cap policy through Job Object CPU-rate control with QueryInformationJobObject read-back.
- Job-wide committed-memory limit subset with read-back.
- Pause/resume explicitly reported as PARTIAL process-level semantics.
- Generic logical temporal-rate control explicitly UNSUPPORTED; CPU service rate is not logical time rate.
- Cross-platform GitHub Actions workflow with Ubuntu and Windows runners.

## Native Windows Evidence

- Workflow run: `32641297667`
- Windows job: `97198681707` (`test-windows-latest`)
- Runner OS: Microsoft Windows Server 2025
- Python: 3.12.10
- `PSS_RUN_WINDOWS_JOB_TESTS=1`
- Result: `39 passed in 0.29s`
- Real integration path exercised: child process -> CreateJobObject -> AssignProcessToJobObject -> SetInformationJobObject CPU hard cap -> QueryInformationJobObject read-back -> ActuationReceipt verification.

Ubuntu matrix job `97198681866` also completed successfully.

## Local Verification

Expected local non-Windows result after M4:

```bash
python -m pytest -q
```

`38 passed, 1 skipped` where the single skip is the opt-in real Windows Job Object test.

Additional verification:

```bash
python -m compileall -q src
python -m pip install -e . --no-deps --no-build-isolation -q
```

## Next

Milestone 5: Linux cgroup v2 Provider — dedicated test subtree only, preserving relative-weight vs hard-limit semantics and verifying realized state by filesystem read-back.
