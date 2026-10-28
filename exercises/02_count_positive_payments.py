"""Early-return debugging exercise: finish the loop before returning."""


def count_positive_payments(payments):
    count = 0

    for payment in payments:
        if payment["amount"] > 0:
            count += 1

    return count


if __name__ == "__main__":
    test_payments = [
        {"type": "MP2", "amount": 200},
        {"type": "Pag-IBIG", "amount": 300},
        {"type": "MP2", "amount": 100},
        {"type": "SSS", "amount": -50},
    ]
    print(count_positive_payments(test_payments))  # Expected: 3
    print(count_positive_payments([]))             # Expected: 0
