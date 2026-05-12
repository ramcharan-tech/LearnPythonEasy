# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LearnPythonEasy is an educational repository for Python fundamentals, Data Structures & Algorithms, and coding interview preparation (Blind 75). It contains standalone Python scripts, reference notes, and study materials — not a packaged application.

## Running Code

There is no build system, package manager, or test framework. Each Python file is a standalone script:

```bash
python <path/to/file.py>
```

Python 3.12 is the target version.

## Repository Structure

- `Basics/` — Python language fundamentals (data types, collections, loops, functions, decorators, generators, file I/O, OOP basics)
- `DataStructures/` — Implementations of linked lists, stacks, queues, trees, graphs, with subdirectories `Graphs/` and `Tree/`
- `algorithms/sorting/` — Sorting algorithm implementations (bubble, insertion, selection)
- `Blind75/` — Curated interview problems; files are numbered with prefix (e.g., `01_two_sum.py`, `02_groupanagrams.py`)
- `PythonOOPSConcepts/` — OOP patterns and examples
- `Dailyproblems/` — Daily coding challenge solutions
- `Practice/` — Miscellaneous practice problems
- `Notes/` — Markdown references (time complexity, tree types, DSA roadmap)
- `Material/` — PDF study resources (not code)
- `Utilities/` — Helper scripts

## Conventions

- Blind75 solutions use numbered prefixes (`NN_problem_name.py`) and typically define a `Solution` class with a method matching LeetCode's signature, followed by a print statement demonstrating usage.
- No linting, formatting, or type-checking tools are configured. Follow existing code style (standard Python conventions, no strict enforcement).
- No dependencies or virtual environment — all code uses the Python standard library only.
