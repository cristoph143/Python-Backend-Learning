
# Define a class named Payment that has the following attributes and methods:
# Attributes:
# - contribution_type: a string representing the type of contribution (e.g., "SSS", "PhilHealth", "Pag-IBIG")
# - amount: a float representing the amount of the contribution
# Methods:
# - is_positive(): a method that returns True if the amount is positive, False otherwise

class Payment:
    # Initialize the Payment class with contribution_type and amount
    def __init__(self, contribution_type: str, amount: float):
        self.contribution_type = contribution_type
        self.amount = amount
        
    # Add is_positive() to return whether the amount is greater than zero.
    def is_positive(self) -> bool:
        return self.amount > 0

    def add_amount(self, additional_amount: float) -> bool:
        if additional_amount > 0:
            self.amount += additional_amount
            return True
        return False


payment = Payment("SSS", 1000)
other_payment = Payment("SSS", 100)
zero_payment = Payment("SSS", 0)
negative_payment = Payment("SSS", -200)
payment.amount = 500

print(zero_payment.is_positive())      # False
print(negative_payment.is_positive())  # False
print(payment.contribution_type)  
print(payment.amount)             
print(payment.is_positive()) 
print(other_payment.amount)  # 100    

payment = Payment("SSS", 1000)

print(payment.add_amount(250))   # True
print(payment.amount)            # 1250

print(payment.add_amount(0))     # False
print(payment.add_amount(-100))  # False
print(payment.amount)            # 1250