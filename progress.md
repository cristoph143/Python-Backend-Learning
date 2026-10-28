# Learning progress

## Current checkpoint — 2026-10-28

Payment class and `add_amount()` reviewed and run successfully. Paused before implementing `total_positive_payments(payments)` while setting up persistent session notes.

Next: in `exercises/03_payment_class.py`, write a function outside the class that accepts Payment objects, calls each object's `is_positive()`, and sums positive `amount` attributes. Examples: amounts 1000, 500, 0, -200 should total 1500; an empty list should return 0. The learner has received requirements and examples, but no implementation. Inspect the file before assuming it is still pending.

Recheck understanding of why `return True` prevents reaching a later `return False`. The tutor explained this; independent restatement has not yet been demonstrated.

## 2026-10-28 — OOP and instance state

- Learner implemented `Payment.__init__`, instance attributes, and `is_positive()` correctly.
- Learner compared `self` to Java's `this`; tutor clarified that it refers to the current instance.
- Zero and negative examples were added after tutor examples; both return False.
- Initial misconception: assigning a new object to the same variable was confused with changing an existing object's attribute.
- After separate-object examples, learner explained that two constructor calls create two objects. Changing one amount leaves the other unchanged.
- Learner implemented `add_amount(additional_amount)` with a positive check, mutation, True on success, and False otherwise.
- Execution confirmed adding 250 changes 1000 to 1250; adding 0 or -100 returns False and preserves 1250.
- Learner described the positive condition and reduced nesting; tutor clarified that immediate return is what prevents fall-through.
- Git: assistant committed and pushed exercise changes to origin/main as `1079ce1`. This does not establish independent Git proficiency.
- Assistance: tutor supplied test examples and explanations; learner supplied method implementations. Independent edge-case design remains unassessed.

The starting assessment below is historical; use the current checkpoint above when resuming.

## 2026-10-28 — Starting assessment

Background: Software Engineering graduate (2024), with an R&D internship involving C/C++, STM32, Qt, debugging, and DLLs. Last regular personal coding: December 2024.

### Demonstrated so far

- Loops, dictionary access, comparisons, and running totals.
- Positive-amount filtering and dictionary grouping, using a tutor scaffold.
- Explanation of why initialization must happen only for a new key.
- Correctly traced an early return: actual count 1, intended count 3.
- Explained moving `return` outside the loop.

### Corrections and reminders

- Dictionary keys are unique; Pag-IBIG needs its own key rather than a second MP2 key.
- Zero and negative amounts must be excluded from this exercise.
- Resetting a total each iteration loses earlier payments.
- Keep display (`print`) separate from returning a result.
- Avoid naming a variable `type`, which shadows a built-in.

### Not yet assessed

OOP, SQL, Git usage, broader data structures, and independent edge-case testing. The provided additional examples do not establish independent testing skill.

### Next step

Complete the Payment class diagnostic in README.md, then explain `self` and show positive, zero, and negative examples.

### Reusable session entry

- Date:
- Topic:
- What I built or solved:
- Evidence I understand it:
- Mistake and fix:
- Hints/documentation/AI used:
- Next step:

### Carry-forward summary

Refreshing Python for a backend career path; target 25 focused hours/week. Payment grouping completed with scaffolding; early-return debugging explained correctly. OOP diagnostic is pending. No framework work yet.
