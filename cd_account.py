# Import the Account class from the Account.py file
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """
    Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        tuple: A tuple containing the updated CD account balance and the interest earned.
    """
    # Create an instance of the `Account` class with the initial balance and interest rate set to 0
    cd_account = Account(balance, 0)

    # Calculate interest earned
    interest_earned = balance * (interest_rate / 12) * months

    # Update the CD account balance by adding the interest earned
    updated_balance = balance + interest_earned

    # Set the updated balance using the instance of the Account class
    cd_account.set_balance(updated_balance)

    # Set the interest earned using the instance of the Account class
    cd_account.set_interest(interest_earned)

    # Return the updated balance and interest earned
    return updated_balance, interest_earned
