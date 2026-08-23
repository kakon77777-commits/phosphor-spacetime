# PHOSPHOR Spacetime Checkpoint — M0 through M5

- Version: `0.1.0a4`
- Date: 2026-08-23
- Repository: `kakon77777-commits/phosphor-spacetime`
- M4 closure: `983caea6a9e0d37d15999a762ca49ef0ee12c3ec`
- M5 implementation: `23764e1ebaf1231a9e40dc5539d72436511825c3`
- M5 validation merge: `99417eaa8d069c55a1c3ef541b7254b340095af6`

## Implemented through M5

- Contracts, Software Spacetime IR, Domain Registry, conflict-preserving projection.
- Authority-bounded CommandIntent, fencing, idempotency, receipts, Mock Provider.
- Registered process Observation Plane.
- Native Windows Job Object Provider with CPU/job-memory policy read-back.
- Linux cgroup v2 Provider for dedicated test subtrees.
- Linux semantics keep `cpu.weight != cpu.max` and `io.weight != io.max`.
- `memory.max`, `cgroup.freeze`, malformed/unknown resource fail-closed paths, and post-actuation read-back are covered.
- Generic OS resource controls never claim native logical-time rate support.

## Native CI Evidence

Workflow run `32643114760`:
- Ubuntu job `97203159145`: Ubuntu 24.04 / Python 3.12.14 / `PSS_RUN_CGROUP_TESTS=1` / `49 passed, 1 skipped` (Windows-only test skipped).
- Windows job `97203159312`: Windows Server 2025 / Python 3.12.10 / `PSS_RUN_WINDOWS_JOB_TESTS=1` / `49 passed, 1 skipped` (Linux-only test skipped).

The Linux native test exercises child PID placement into `/sys/fs/cgroup/phosphor-spacetime-ci`, `cpu.weight=200`, `cpu.max=50000 100000`, filesystem read-back, and receipt verification.

## Next

M6 Synthetic Multi-Temporal Runtime: logical clock, explicit requested/realized rate semantics, discrete event queue, event jump, snapshot/restore, and deterministic state hash.
