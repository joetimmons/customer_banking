"""Imports the SavingsAccount class and attributes from the Account.py file."""
# Correct the import statement to import SavingsAccount
from customer_banking.account import SavingsAccount

def create_savings_account(balance, interest_rate, months):
    """
    Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        tuple: A tuple containing the updated savings account balance and the interest earned.
    """
    # Create an instance of the SavingsAccount class with the balance and interest rate set to 0
    savings_account = SavingsAccount(balance, 0)

    # Calculate interest earned
    interest_earned = balance * (interest_rate / 12) * months

    # Update the savings account balance by adding the interest earned
    updated_balance = balance + interest_earned

    # Set the updated balance using the instance of the SavingsAccount class
    savings_account.set_balance(updated_balance)

    # Set the interest earned using the instance of the SavingsAccount class
    savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned
    return updated_balance, interest_earned
