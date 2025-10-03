import sys
from bank_account import BankAccount

def main():
    """Interface to interact with the BankAccount class via command line."""
    try:
        account = BankAccount(100)  # starting balance

        if len(sys.argv) < 2:
            print("Usage: python main-0.py <command>:<amount>")
            print("Commands: deposit, withdraw, display")
            sys.exit(1)

        # Split command and optional amount
        command, *params = sys.argv[1].split(':')
        amount = float(params[0]) if params else None

        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount}")
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient funds.")
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

