"""Summarize positive fictional payments by contribution type.

Based on my exercise completed with tutor scaffolding.
Assumes each record has a string type and a numeric amount.
"""


def summarize_payments(payments):
    totals = {}

    for payment in payments:
        contribution_type = payment["type"]
        amount = payment["amount"]

        if amount > 0:
            if contribution_type not in totals:
                totals[contribution_type] = 0
            totals[contribution_type] += amount

    return totals


if __name__ == "__main__":
    payments = [
        {"type": "SSS", "amount": 1500},
        {"type": "MP2", "amount": 500},
        {"type": "SSS", "amount": 1500},
        {"type": "PhilHealth", "amount": 0},
        {"type": "MP2", "amount": -200},
    ]
    print(summarize_payments(payments))
    # Expected: {"SSS": 3000, "MP2": 500}
