# Personal Finance Tracker - Python

transactions = []


def add_transaction():
    print("\n--- Add Transaction ---")

    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    print("1. Income")
    print("2. Expense")

    choice = input("Select type: ")

    if choice == "1":
        transaction_type = "Income"
    elif choice == "2":
        transaction_type = "Expense"
    else:
        print("Invalid choice!")
        return

    category = input("Enter category: ")

    transaction = {
        "description": description,
        "amount": amount,
        "type": transaction_type,
        "category": category
    }

    transactions.append(transaction)

    print("Transaction added successfully!")


def show_transactions():
    print("\n--- Transactions ---")

    if len(transactions) == 0:
        print("No transactions added yet.")
        return

    for i, transaction in enumerate(transactions, 1):

        print("\nTransaction", i)
        print("Description :", transaction["description"])
        print("Category    :", transaction["category"])
        print("Type        :", transaction["type"])
        print("Amount      : ₹", transaction["amount"])


def show_summary():

    total_income = 0
    total_expense = 0

    for transaction in transactions:

        if transaction["type"] == "Income":
            total_income += transaction["amount"]

        elif transaction["type"] == "Expense":
            total_expense += transaction["amount"]

    balance = total_income - total_expense

    print("\n--- Financial Summary ---")

    print("Total Income  : ₹", total_income)
    print("Total Expense : ₹", total_expense)
    print("Balance       : ₹", balance)


def delete_transaction():

    show_transactions()

    if len(transactions) == 0:
        return

    number = int(input("\nEnter transaction number to delete: "))

    if 1 <= number <= len(transactions):

        transactions.pop(number - 1)

        print("Transaction deleted successfully!")

    else:
        print("Invalid transaction number!")


def main():

    while True:

        print("\n==============================")
        print("   PERSONAL FINANCE TRACKER")
        print("==============================")

        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Summary")
        print("4. Delete Transaction")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_transaction()

        elif choice == "2":
            show_transactions()

        elif choice == "3":
            show_summary()

        elif choice == "4":
            delete_transaction()

        elif choice == "5":
            print("Thank you for using Personal Finance Tracker!")
            break

        else:
            print("Invalid choice! Please try again.")


main()
