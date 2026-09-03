import csv
from datetime import date
from collections import defaultdict

FILE_NAME = "expenses.csv"


def ensure_file():
    try:
        with open(FILE_NAME, "r", newline=""):
            pass
    except FileNotFoundError:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "category", "amount", "description"])


def add_expense():
    expense_date = input("Date (YYYY-MM-DD, blank for today): ").strip()
    if not expense_date:
        expense_date = str(date.today())

    category = input("Category: ").strip().title()
    description = input("Description: ").strip()

    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid positive amount.")
        return

    with open(FILE_NAME, "a", newline="") as file:
        csv.writer(file).writerow(
            [expense_date, category, f"{amount:.2f}", description]
        )

    print("Expense added successfully.")


def read_expenses():
    with open(FILE_NAME, "r", newline="") as file:
        return list(csv.DictReader(file))


def view_expenses():
    expenses = read_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\nDate         Category          Amount      Description")
    print("-" * 60)

    for expense in expenses:
        print(
            f"{expense['date']:<12}"
            f"{expense['category']:<18}"
            f"₹{float(expense['amount']):<10.2f}"
            f"{expense['description']}"
        )


def total_expenses():
    expenses = read_expenses()
    total = sum(float(expense["amount"]) for expense in expenses)
    print(f"Total spending: ₹{total:.2f}")


def category_summary():
    expenses = read_expenses()
    summary = defaultdict(float)

    for expense in expenses:
        summary[expense["category"]] += float(expense["amount"])

    if not summary:
        print("No expenses found.")
        return

    print("\nCategory-wise spending:")
    for category, amount in sorted(summary.items()):
        print(f"{category}: ₹{amount:.2f}")


def main():
    ensure_file()

    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
