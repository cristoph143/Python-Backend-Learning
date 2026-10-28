# Python fundamentals

These are tutor-provided reference notes. Rewrite them in my own words and add my own examples.

## Dictionaries

Keys are unique. Setting an existing key replaces its value. To group payments, create a key once, then add to its running total.

## Filtering

`amount > 0` includes positive amounts and excludes both zero and negative amounts.

## Return and print

`return` sends a value to the caller and immediately exits the function. `print` displays a value. Keeping printing outside a calculation function makes the result reusable.

## Indentation and loops

A return inside a loop ends the function during an iteration. A return after the loop lets every record be processed. An empty list skips the loop entirely.

## Naming

Use `payment` for one record. Avoid `type` as a variable name because it is already a Python built-in. Use snake_case for Python function and variable names.

## My explanations — fill these in

- Why initialize a category only once?
- What happens for an empty payment list?
- How does the function avoid modifying the original list?
- What does `self` represent? (After the OOP exercise.)
