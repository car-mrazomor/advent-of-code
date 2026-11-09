#!/usr/bin/env python3
"""Fetch a puzzle (as text) and its input, cached locally. Inputs are never committed.

    python3 aoc.py 2019 1        # writes 2019/day01/input.txt, prints the puzzle text
"""
import html
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CACHE = Path.home() / ".cache" / "advent-of-code"
UA = "github.com/car-mrazomor/advent-of-code"


def session():
    for path in (Path.home() / ".config" / "aoc-session", Path.home() / ".config" / "aoc-session."):
        if path.exists():
            return re.sub(r"^session=", "", path.read_text().strip(), flags=re.I)
    return os.environ["AOC_SESSION"]


def get(url, cache):
    if cache.exists():
        return cache.read_text()
    time.sleep(1.5)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Cookie": f"session={session()}"})
    text = urllib.request.urlopen(req).read().decode()
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(text)
    return text


def to_text(page):
    articles = re.findall(r"<article[^>]*>(.*?)</article>", page, re.S)
    answers = re.findall(r"Your puzzle answer was <code>(.*?)</code>", page)
    parts = []
    for body in articles:
        body = re.sub(r"<pre><code>(.*?)</code></pre>", lambda m: "\n```\n" + m[1] + "```\n", body, flags=re.S)
        body = re.sub(r"<li>", "\n- ", body)
        body = re.sub(r"</?(p|h2|ul)>", "\n", body)
        text = html.unescape(re.sub(r"<[^>]+>", "", body))
        parts.append(re.sub(r"\n\s*\n(\s*\n)+", "\n\n", text).strip())
    return parts, answers


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    year, day = int(args[0]), int(args[1])
    folder = ROOT / str(year) / f"day{day:02d}"
    base = f"https://adventofcode.com/{year}/day/{day}"
    get(base + "/input", folder / "input.txt")
    page_cache = CACHE / str(year) / f"{day:02d}.html"
    if "--refresh" in sys.argv and page_cache.exists():
        page_cache.unlink()
    parts, answers = to_text(get(base, page_cache))
    for i, part in enumerate(parts, 1):
        print(f"===== part {i} =====\n{part}\n")
    for i, answer in enumerate(answers, 1):
        print(f"answer {i}: {answer}")


if __name__ == "__main__":
    main()
