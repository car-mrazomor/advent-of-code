#!/usr/bin/env python3
"""Run one day's solution on its input:  python3 run.py 2019 1  (input from 2019/day01/input.txt on stdin)."""
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def command(source, build):
    kind = source.suffix
    if kind == ".py":
        return [sys.executable, str(source)]
    exe = str(Path(build) / "solution")
    if kind == ".c":
        subprocess.run(["cc", "-O2", "-o", exe, str(source), "-lm"], check=True)
    elif kind == ".s":
        subprocess.run(["cc", "-o", exe, str(source)], check=True)
    elif kind == ".rs":
        subprocess.run(["rustc", "-O", "--edition", "2021", "-o", exe, str(source)], check=True)
    elif kind == ".go":
        subprocess.run(["go", "build", "-o", exe, str(source)], check=True)
    else:
        raise SystemExit(f"don't know how to run {source.name}")
    return [exe]


def main():
    year, day = sys.argv[1], int(sys.argv[2])
    folder = ROOT / year / f"day{day:02d}"
    source = next(folder.glob("solution.*"))
    data = sys.stdin.read() if len(sys.argv) > 3 and sys.argv[3] == "-" else (folder / "input.txt").read_text()
    with tempfile.TemporaryDirectory() as build:
        result = subprocess.run(command(source, build), input=data, text=True, cwd=folder)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
