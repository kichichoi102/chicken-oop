# PEP 484 - Type Hints/Annotations

## Introduction:
- Followed conventions from [PEP 484](https://peps.python.org/pep-0484/), added type hints in all appropriate places
- Used Mypy library to check for types in codebase.

## Mypy:
- Mypy is a static type checker for Python.
- type hints according to PEP 484

## Usage:
- `~/chicken-coop$ mypy --strict --enable-incomplete-feature=Unpack <path_to_file>`