import re
import sys

REQUIRED = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
RULES = {
    "byr": lambda v: re.fullmatch(r"\d{4}", v) and 1920 <= int(v) <= 2002,
    "iyr": lambda v: re.fullmatch(r"\d{4}", v) and 2010 <= int(v) <= 2020,
    "eyr": lambda v: re.fullmatch(r"\d{4}", v) and 2020 <= int(v) <= 2030,
    "hgt": lambda v: (m := re.fullmatch(r"(\d+)(cm|in)", v)) and
                     (150 <= int(m[1]) <= 193 if m[2] == "cm" else 59 <= int(m[1]) <= 76),
    "hcl": lambda v: re.fullmatch(r"#[0-9a-f]{6}", v),
    "ecl": lambda v: v in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda v: re.fullmatch(r"\d{9}", v),
}

passports = [dict(field.split(":") for field in block.split()) for block in sys.stdin.read().split("\n\n")]
complete = [p for p in passports if REQUIRED <= p.keys()]
print(len(complete))
print(sum(all(RULES[k](p[k]) for k in REQUIRED) for p in complete))
