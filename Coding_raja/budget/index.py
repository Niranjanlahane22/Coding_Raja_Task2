import os

# Define the path to the file where transactions will be stored
DATA_FILE_PATH = 'budget_data.txt'

def load_transactions():
    """Load transactions from the file."""
    if not os.path.exists(DATA_FILE_PATH):
        return []

    with open(DATA_FILE_PATH, 'r') as file:
        transactions = [line.strip().split(',') for line in file]
    return [(t[0], float(t[1]), t[2]) for t in transactions]

def save_transaction(transaction_type, amount, category):
    """Save a new transaction to the file."""
    with open(DATA_FILE_PATH, 'a') as file:
        file.write(f'{transaction_type},{amount},{category}\n')

def add_transaction():
    """Add a new transaction."""
    transaction_type = input("Enter transaction type (income/expense): ").lower()
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    save_transaction(transaction_type, amount, category)
    print("Transaction added successfully.")

def calculate_balance(transactions):
    """Calculate the current balance based on transactions."""
    income = sum(amount for t_type, amount, category in transactions if t_type == 'income')
    expenses = sum(amount for t_type, amount, category in transactions if t_type == 'expense')
    return income - expenses

def show_transactions(transactions):
    """Show all transactions and the current balance."""
    for t_type, amount, category in transactions:
        print(f'{t_type.title()}: ${amount} - {category}')
    print(f"\nCurrent Balance: ${calculate_balance(transactions)}")

def show_insights(transactions):
    """Show insights on spending."""
    categories = {}
    for t_type, amount, category in transactions:
        if t_type == 'expense':
            if category not in categories:
                categories[category] = amount
            else:
                categories[category] += amount

    print("\nExpenses by Category:")
    for category, amount in categories.items():
        print(f'{category}: ${amount}')

def main():
    transactions = load_transactions()

    while True:
        print("\n--- Budget Tracker ---")
        print("1. Add a new transaction")
        print("2. Show all transactions")
        print("3. Show spending insights")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_transaction()
            transactions = load_transactions()  # Reload transactions after adding a new one
        elif choice == '2':
            show_transactions(transactions)
        elif choice == '3':
            show_insights(transactions)
        elif choice == '4':
            print("Visite Again11!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
