# Python Backend Learning

My learning journal and exercises as I refresh computer science fundamentals and prepare for junior Python backend roles in Dubai.

## Study schedule

- Five working days: 3 focused hours per day.
- Two off days: 5 focused hours per day.
- Target: 25 focused hours weekly, with breaks and recovery time.

## Current focus

Python fundamentals and basic OOP. Payment class and amount updates reviewed; next exercise: sum positive payments from a list of objects. Read `progress.md` for the exact resume checkpoint and `ROADMAP.md` for the full journey. `AGENTS.md` guides future tutoring sessions.

## Files

- `exercises/01_payment_summary.py`: group positive payments by contribution type.
- `exercises/02_count_positive_payments.py`: corrected early-return exercise.
- `exercises/03_payment_class.py`: instance attributes, positive checks, and amount updates.
- `AGENTS.md`: instructions for continuing tutoring across sessions.
- `ROADMAP.md`: learning stages and milestone criteria.
- `progress.md`: evidence of learning and next steps.
- `notes/python_fundamentals.md`: reference notes to rewrite in my own words.

## Run the exercises

Install Python 3, open a terminal in this folder, and run:

```bash
python exercises/01_payment_summary.py
python exercises/02_count_positive_payments.py
```

On Windows, use `py` if `python` is unavailable. No external packages are required.

## Next exercise: list of Payment objects

In `exercises/03_payment_class.py`, define `total_positive_payments(payments)` outside the class:

1. Accept a list of Payment objects.
2. Use each object's `is_positive()` method to decide whether to include it.
3. Add positive `amount` values and return the total.
4. Verify amounts 1000, 500, 0, -200 produce 1500.
5. Verify an empty list produces 0.

## Longer-term direction

Python → SQL/PostgreSQL → HTTP and Django → authentication and permissions → testing → Linux, Docker, deployment, and CI.

Keep algorithms, data structures, networking, operating systems, and security alongside project work. Adjust the pace after assessments.

Project ideas: an OFW contribution management application and a daily-report automation service. Use fictional data only.

## Track with GitHub

Repository: https://github.com/cristoph143/Python-Backend-Learning

The repository is configured and exercise changes have been pushed to `main`. Typical commands for future checkpoints:

```bash
git status
git diff
git add exercises/03_payment_class.py
git commit -m "Describe the completed learning checkpoint"
git push origin main
```

Review changes before staging. Include updated learning notes when appropriate.

Record assistance honestly. A completed exercise counts toward understanding when I can explain, modify, and test it independently.
