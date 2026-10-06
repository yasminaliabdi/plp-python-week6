# Week 6 Assignment: Safe Functions & Unbreakable Program

## Files

- **safe_tools.py** - Contains three safe functions (`safe_divide`, `safe_number`, `get_field`) that use `try / except` to handle errors gracefully.
- **unbreakable.py** - A program that keeps running even when the user enters bad input.

## Why an `if` Check Cannot Catch "abc" on Its Own

An `if` statement can only compare values — it cannot detect when a value has the wrong type. For example, `int("abc")` raises a `ValueError` at runtime that an `if` statement cannot prevent. Only `try / except` can catch that error and handle it gracefully.

## How to Run

1. Run `python safe_tools.py` to test the safe functions.
2. Run `python unbreakable.py` to test the unbreakable program.