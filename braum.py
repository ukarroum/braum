import argparse
from dataclasses import dataclass
from pathlib import Path
from enum import Enum


class WebSourceType(Enum):
    DJANGO = 1


@dataclass
class WebSourceRoot:
    root: Path
    type: WebSourceType


def scan_source():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Braum: An experimental web vulnerability scanner tool")
    parser.add_argument("--src-path", help="path to the source logs")
    parser.add_argument("--hostname", help="path to the hostname")

    args = parser.parse_args()
