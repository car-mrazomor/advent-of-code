#!/usr/bin/env python3
"""submit answer automatically from machine"""

import argparse
import os
import re
import requests
from dotenv import load_dotenv
from selectolax.lexbor import LexborHTMLParser as lp

load_dotenv()
SESSION_KEY = os.environ.get("SESSION_KEY")
MAIN_URL = "https://adventofcode.com"


class WrongSessionKey(Exception):
    pass


parser = argparse.ArgumentParser()
parser.add_argument("answer")
parser.add_argument("day")
parser.add_argument("level")
parser.add_argument("--year", default=None)


def _prepare_headers() -> dict[str, str]:
    return {
        "Cookie": f"session={SESSION_KEY}",
        "User-Agent": "myproject/1.0 (+https://github.com/car-mrazomor/advent-of-code)",
    }


def _request(method, path="/", data=None):
    headers: dict = _prepare_headers()
    res = requests.request(
        method=method, url=MAIN_URL + path, headers=headers, data=data
    )
    res.raise_for_status()

    return res


def check_session() -> str:
    res = _request(method="GET")
    tree = lp(res.text)

    return tree.text()


def submit_answer(answer, day, level, year=None):
    url_path: str = f"/{year}/day/{day}/answer" if year else f"/day/{day}/answer"
    data: dict = {"level": level, "answer": answer}
    res = _request(method="POST", path=url_path, data=data)
    tree = lp(res.text)

    if "That's not the right answer." in tree.text():
        return "not_correct"

    if "You gave an answer too recently;" in tree.text():
        match = re.search(r"have (\d+)m\s+(\d+)s left", tree.text())
        if not match:
            match = re.search(r"have (\d+)s left", tree.text())
            if not match:
                return "wait_unknown"
            return f"wait_{match.group(1)}s"
        return f"wait_{match.group(1)}m_{match.group(2)}s"

    return "solved"


def main(args):
    if not check_session():
        raise WrongSessionKey("Expired session or wrong session key.")

    print(submit_answer(args.answer, args.day, args.level, args.year))


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
