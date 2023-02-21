# PEP 8 - Style Guide Followed

## Introduction:
This document gives coding conventions for the Python code comprising the standard library in the main Python distribution. 

## Conventions:
- Indentations: Used tabs (4 spaces)
- Max line length: used 100 chars
- Blank Lines: surround top-level fxn and class with 2 blank lines
- Comments: see `./docs/conventions/pep_257.md`

## Pylint
Pylint is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for bad code smells.

## Usage
`pylint <path_to_file>`

## Imports:
- In my current projects, we follow the rule of absolute imports.
- I know you can bundle directories import multiple files from one directory by adding them to the `__init__.py` file, but I decided not to follow this.
- Used absolute imports for all files.