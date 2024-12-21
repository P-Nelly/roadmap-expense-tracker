import argparse
from tabulate import tabulate
import json
from datetime import date, datetime
import os

class Expense():
    def __init__(self, id, amount, description) -> None:
        self.amount = amount
        self.id = id
        self.description = description
        self.date = datetime.today().strftime('%Y-%m-%d')

class Expense_manager():
    def __init__(self, expenses_file) -> None:
        self.expenses_file = expenses_file
        self.expenses = self.load_expenses()

    def load_expenses(self) -> list[Expense]:
        if not os.path.exists(self.expenses_file):
            print(f"saved file at {self.expenses_file} not found")
            return []
        try:
            with open(self.expenses_file, 'r') as file:
                expenses_data = json.load(file)
                return [Expense(**expense) for expense in expenses_data] 
        except Exception:
            print('Failed to load JSON')
            return []

    def save_expenses(self) -> None:
        with open(self.expenses_file, 'w') as file:
            json.dump([expense.__dict__ for expense in self.expenses], file, indent=4)

    def get_id(self) -> int:
        used_ids = [expense.id for expense in self.expenses]
        id = 0
        while id in used_ids:
            id += 1
        return id

    def create_expense(self, amount, description) -> Expense:
        id = self.get_id()
        new_expense = Expense(id, amount, description)
        self.expenses.append(new_expense)
        self.save_expenses()
        return new_expense

    def delete_expense(self, id):
        self.expenses = [expense for expense in self.expenses if expense.id != id]
        self.save_expenses()

    def list_expenses(self):
        if not self.expenses:
            print("No expenses to print")
            return
        headers = ["ID", "Date", "Description", "Amount"]
        table = [[expense.id, expense.date, expense.description, expense.amount] for expense in self.expenses]
        print(tabulate(table, headers, tablefmt='simple_outline'))

    def month_summary(self, month):
        sum = 0
        for expense in self.expenses:
            expense_month = datetime.strptime(expense.date, '%Y-%m-%d').month
            if expense_month == month:
                sum += int(expense.amount)
        print(f'Total expenditure for the month: {sum}')

def main():
    parser = argparse.ArgumentParser(description='Expense Tracker CLI')
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('--description', required=True, help='Description of the expense')
    add_parser.add_argument('--amount', type=float, required=True, help='Amount of the expense')

    # List command
    subparsers.add_parser('list', help='List all expenses')

    # Summary command
    summary_parser = subparsers.add_parser('summary', help='Show expense summary')
    summary_parser.add_argument('--month', type=int, help='Show summary for specific month')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete an expense')
    delete_parser.add_argument('--id', type=int, required=True, help='ID of the expense to delete')

    args = parser.parse_args()
    
    expense_manager = Expense_manager('expenses.json')
    print(f'Current local time is: {datetime.now().isoformat()}')

    if args.command == 'add':
        if args.amount <= 0:
            print("Error: Amount must be greater than zero.")
            return
        expense = expense_manager.create_expense(args.amount, args.description)
        print(f"Expense added successfully (ID: {expense.id})")
    
    elif args.command == 'list':
        if not expense_manager.expenses:
            print("No expenses to list.")
            return
        expense_manager.list_expenses()
    
    elif args.command == 'summary':
        if not expense_manager.expenses:
            print("No expenses recorded.")
            return
        if args.month:
            if args.month < 1 or args.month > 12:
                print("Error: Month must be between 1 and 12.")
                return
            expense_manager.month_summary(args.month)
        else:
            total = sum(float(expense.amount) for expense in expense_manager.expenses)
            print(f"Total expenses: ${total:.2f}")
    
    elif args.command == 'delete':
        if args.id not in [expense.id for expense in expense_manager.expenses]:
            print(f"Error: No expense found with ID {args.id}.")
            return
        expense_manager.delete_expense(args.id)
        print("Expense deleted successfully")

if __name__ == '__main__':
    main()
