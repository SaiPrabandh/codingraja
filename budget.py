import json

def load_transactions(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_transactions(transactions, filename):
    with open(filename, 'w') as file:
        json.dump(transactions, file, indent=4)

def add_transaction(trans_type, category, amount, transactions):
    transactions.append({"type": trans_type, "category": category, "amount": amount})
    save_transactions(transactions, filename)
    print("Transaction added successfully!")

def calculate_total(transactions, trans_type):
    total = 0
    for transaction in transactions:
        if transaction["type"] == trans_type:
            total += transaction["amount"]
    return total

def calculate_budget(income, expenses):
    return income - expenses

def analyze_expenses(transactions):
    categories = {}
    for transaction in transactions:
        if transaction["type"] == "Expense":
            category = transaction["category"]
            amount = transaction["amount"]
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount
    
    print("Expense Analysis:")
    for category, amount in categories.items():
        print(f"{category}: ${amount}")

def main():
    global filename

    filename = "transactions.json"
    transactions = load_transactions(filename)

    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Budget")
        print("4. Analyze Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_transaction("Expense", category, amount, transactions)
        elif choice == "2":
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            add_transaction("Income", category, amount, transactions)
        elif choice == "3":
            total_income = calculate_total(transactions, "Income")
            total_expenses = calculate_total(transactions, "Expense")
            remaining_budget = calculate_budget(total_income, total_expenses)
            print("\nBudget Summary:")
            print(f"Total Income: ${total_income}")
            print(f"Total Expenses: ${total_expenses}")
            print(f"Remaining Budget: ${remaining_budget}")
        elif choice == "4":
            analyze_expenses(transactions)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
