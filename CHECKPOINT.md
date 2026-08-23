# PHOSPHOR Spacetime Checkpoint — M0 through M9

- Version: `0.1.0a8`
- Date: 2026-08-23
- Repository: `kakon77777-commits/phosphor-spacetime`
- M8 closure head: `8937af42e3916be5c1073063ea387ed1b1946356`
- M9 feature merge: `773a23e4a846e3e944691a278569cd07e74ed3b8`

## Implemented through M9

M0–M8 contracts, IR, observation, authority, providers, Synthetic Runtime, Rule Governor, and schema-bounded AI Policy Adapter remain intact.

M9 adds:

- `BenchmarkHarness` with manifest-first run creation.
- A–E synthetic correctness workloads: Anchored, Elastic CPU, Event-Sparse, Causal DAG, and Mixed.
- Formal baselines: `B0_NATIVE`, `B1_FIXED`, `B2_RULE`, `B3_AI`.
- B3 always routes through the M8 `AIPolicyAdapter`; malformed AI output is retained as deterministic Rule fallback evidence.
- Run artifacts: manifest, config, metrics, correctness, command-intent log, actuation-receipt log, and summary.
- Failed workload execution is retained as an invalid run rather than discarded.
- Invalid runs remain visible in comparison reports but do not contribute to numeric aggregates.
- Comparison compatibility rejects mixed-workload comparisons and warns when baseline seed sets differ.
- CLI commands: `pss run`, `pss matrix`, and `pss compare`.
- Package metadata is synchronized: `phosphor_spacetime.__version__ == pyproject version == 0.1.0a8`.

## M9 Correctness Evidence

- Local M9 targeted benchmark tests before closure: `16 passed`.
- Local package-metadata closure test: `1 passed` after an intentional RED demonstrating the old `0.1.0a0` / `0.1.0a7` version mismatch.
- Full local closure regression: `117 passed, 2 skipped` (two platform-native tests).
- A–E × B0–B3 synthetic matrix smoke: `20/20 valid`.
- Event-Sparse B0 and B2 preserve the same application state hash while B0 performs 1000 tick iterations and B2 event-jump performs 0 tick iterations in the synthetic reference workload.
- `pss --help` is available after editable install and exposes `run / matrix / compare`.
- M9 hard gates cover reproducibility, correctness, artifact integrity, invalid-run retention, and comparison compatibility. They do not require performance superiority.

## CI Evidence

PR validation workflow run `32649039908`:

- Ubuntu job `97217661925`: `117 passed, 1 skipped`; Linux cgroup v2 native path executed.
- Windows job `97217662030`: `117 passed, 1 skipped`; Windows Job Object native path executed.

## Empirical Boundary

M9 does **not** claim that `B2 > B1` or `B3 > B2`. Those remain falsifiable empirical hypotheses for repeated benchmark runs. Performance values are evidence, not M9 hard pass criteria.

## Next

M10 Gate Runner + Failure Injection: encode hard Gate 0–6 checks, inject observer/provider/AI/control failures, verify fail-closed mutation and host survival, and expose `pss gate` before the first formal benchmark book.
