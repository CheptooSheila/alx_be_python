class BankAccount:
    """A simple bank account class demonstrating OOP principles."""

    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw the specified amount if sufficient funds exist."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance}")

