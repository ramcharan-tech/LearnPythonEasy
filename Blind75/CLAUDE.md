# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Blind75 Problem File Conventions

Each file follows this structure:

1. **Filename**: `NN_problem_name.py` (e.g., `01_two_sum.py`, `02_group_anagrams.py`)
2. **Header**: Problem title with LeetCode ID (e.g., `# 1. Two Sum (LeetCode #1)`)
3. **Mnemonic/Intuition Block**: A few lines at the top (after the title) to memorize the solution approach in a mnemonic way. This should:
   - Capture the core insight or pattern in one memorable phrase
   - Explain the "aha" moment that unlocks the solution
   - Help build creative problem-solving intuition for similar problems in coding challenges
4. **Problem Statement**: Brief description with examples
5. **Multiple Solutions**: One sub-optimal and multiple optimal approaches (skip brute force), each with:
   - Approach name and explanation
   - Time and space complexity
   - The implementation as a method in a `Solution` class (matching LeetCode signature)
6. **Demo**: A print statement at the bottom showing usage

## Goal

The mnemonic block is the key differentiator — it trains pattern recognition so that during a timed challenge, you recall the technique instantly rather than deriving it from scratch.
