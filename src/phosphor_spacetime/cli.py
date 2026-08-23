from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from phosphor_spacetime.benchmark.harness import BASELINES, BenchmarkHarness
from phosphor_spacetime.metrics.compare import compare_run_dirs
from phosphor_spacetime.gates import GateRunner


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pss", description="PHOSPHOR Spacetime benchmark harness")
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run")
    run.add_argument("workload")
    run.add_argument("--baseline", required=True, choices=BASELINES)
    run.add_argument("--runs-root", default="runs")
    run.add_argument("--git-commit", default="UNKNOWN")
    run.add_argument("--seed", type=int, default=42)
    run.add_argument("--repeat-index", type=int, default=0)

    matrix = sub.add_parser("matrix")
    matrix.add_argument("workload")
    matrix.add_argument("--runs-root", default="runs")
    matrix.add_argument("--git-commit", default="UNKNOWN")
    matrix.add_argument("--seed", type=int, default=42)
    matrix.add_argument("--repeat-index", type=int, default=0)

    compare = sub.add_parser("compare")
    compare.add_argument("run_dirs", nargs="+")
    compare.add_argument("--output")

    gate = sub.add_parser("gate")
    gate.add_argument("--work-root", default="runs/gates")
    gate.add_argument("--git-commit", default="UNKNOWN")
    gate.add_argument("--output")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(list(argv) if argv is not None else None)
    if args.command == "run":
        record = BenchmarkHarness(runs_root=args.runs_root, git_commit=args.git_commit).run(
            args.workload,
            args.baseline,
            random_seed=args.seed,
            repeat_index=args.repeat_index,
        )
        print(record.run_dir)
        return 0 if record.valid else 2
    if args.command == "matrix":
        records = BenchmarkHarness(runs_root=args.runs_root, git_commit=args.git_commit).run_matrix(
            args.workload,
            random_seed=args.seed,
            repeat_index=args.repeat_index,
        )
        print(json.dumps([str(record.run_dir) for record in records], indent=2))
        return 0 if all(record.valid for record in records) else 2
    if args.command == "compare":
        report = compare_run_dirs(args.run_dirs)
        encoded = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        if args.output:
            Path(args.output).write_text(encoded, encoding="utf-8")
        else:
            print(encoded, end="")
        return 0
    if args.command == "gate":
        report = GateRunner(work_root=args.work_root, git_commit=args.git_commit).run()
        encoded = json.dumps(report.model_dump(mode="json"), ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        if args.output:
            Path(args.output).write_text(encoded, encoding="utf-8")
        else:
            print(encoded, end="")
        return 0 if report.passed else 3
    raise RuntimeError("unreachable")


if __name__ == "__main__":
    raise SystemExit(main())
