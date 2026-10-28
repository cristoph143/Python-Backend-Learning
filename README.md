# Python Backend Learning

My learning journal and exercises as I refresh computer science fundamentals and prepare for junior Python backend roles in Dubai.

## Study schedule

- Five working days: 3 focused hours per day.
- Two off days: 5 focused hours per day.
- Target: 25 focused hours weekly, with breaks and recovery time.

## Current focus

Python fundamentals: functions, loops, dictionaries, filtering, debugging, and basic OOP. Next diagnostic: implement a `Payment` class independently.

## Files

- `exercises/01_payment_summary.py`: group positive payments by contribution type.
- `exercises/02_count_positive_payments.py`: corrected early-return exercise.
- `progress.md`: evidence of learning and next steps.
- `notes/python_fundamentals.md`: reference notes to rewrite in my own words.

## Run the exercises

Install Python 3, open a terminal in this folder, and run:

```bash
python exercises/01_payment_summary.py
python exercises/02_count_positive_payments.py
```

On Windows, use `py` if `python` is unavailable. No external packages are required.

## Next exercise: Payment class

When ready, create `exercises/03_payment_class.py` yourself:

1. Define a class named `Payment`.
2. Store `contribution_type` and `amount` using `__init__`.
3. Add `is_positive()` returning whether the amount is greater than zero.
4. Try positive, zero, and negative amounts.
5. Explain what `self` represents.

## Longer-term direction

Python → SQL/PostgreSQL → HTTP and Django → authentication and permissions → testing → Linux, Docker, deployment, and CI.

Keep algorithms, data structures, networking, operating systems, and security alongside project work. Adjust the pace after assessments.

Project ideas: an OFW contribution management application and a daily-report automation service. Use fictional data only.

## Track with GitHub

Create an empty GitHub repository named `python-backend-learning`. In this folder run:

```bash
git init
git add .
git commit -m "Add payment summary and early-return debugging exercises"
git branch -M main
```

Then use the remote URL and push instructions GitHub displays for your new repository. This starter package has not been uploaded to GitHub.

Record assistance honestly. A completed exercise counts toward understanding when I can explain, modify, and test it independently.
