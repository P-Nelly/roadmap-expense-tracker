import argparse
from tabulate import tabulate
import json
from datetime import date, datetime
import os

class Expense():
    def __init__(self, id, amount, description, date=None) -> None:
        self.amount = amount
        self.id = id
        self.description = description
        self.date = date if date else datetime.today().strftime('%Y-%m-%d')

class Expense_manager():
    def __init__(self, expenses_file) -> None:
        self.expenses_file = expenses_file
        self.expenses = self.load_expenses()

    def load_expenses(self) -> list[Expense]:
        try:
            if not os.path.exists(self.expenses_file):
                print(f"Creating new expenses file at {self.expenses_file}")
                try:
                    # Create an empty expenses file with proper permissions
                    with open(self.expenses_file, 'x') as file:
                        json.dump([], file)
                except (IOError, PermissionError) as e:
                    print(f"Error creating expenses file: {str(e)}")
                    return []
                return []

            with open(self.expenses_file, 'r') as file:
                try:
                    expenses_data = json.load(file)
                    if not isinstance(expenses_data, list):
                        print("Warning: Expenses file contains invalid data format. Expected a list.")
                        return []
                    return [Expense(**expense) for expense in expenses_data]
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from expenses file: {str(e)}")
                    return []
                except (KeyError, TypeError) as e:
                    print(f"Error parsing expense data: {str(e)}")
                    return []
        except (IOError, PermissionError) as e:
            print(f"Error accessing expenses file: {str(e)}")
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

    def update_expense(self, id, amount, description):
        for expense in self.expenses:
            if expense.id == id:
                if amount is not None:
                    expense.amount = amount
                if description is not None:
                    expense.description = description
                break
        self.save_expenses()

def clear_terminal():
    os.system('clear')

def interactive_mode(expense_manager):
    """Interactive mode for the expense tracker.
    
    Provides a menu-driven interface with all features available in CLI mode.
    """
    while True:
        clear_terminal()
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Monthly Summary")
        print("4. Delete Expense")
        print("5. Update Expense")
        print("6. Total Summary")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == "1":
            clear_terminal()
            description = input("Enter expense description: ")
            while True:
                try:
                    amount = float(input("Enter amount: "))
                    if amount <= 0:
                        print("Amount must be greater than zero.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
            
            expense = expense_manager.create_expense(amount, description)
            print(f"\nExpense added successfully (ID: {expense.id})")
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            clear_terminal()
            print("\nCurrent Expenses:\n")
            expense_manager.list_expenses()
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            clear_terminal()
            while True:
                try:
                    month = int(input("Enter month (1-12): "))
                    if 1 <= month <= 12:
                        print()
                        expense_manager.month_summary(month)
                        break
                    print("Month must be between 1 and 12.")
                except ValueError:
                    print("Please enter a valid number.")
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            clear_terminal()
            if not expense_manager.expenses:
                print("No expenses to delete.")
                input("\nPress Enter to continue...")
                continue
                
            print("Current Expenses:\n")
            expense_manager.list_expenses()
            print()
            while True:
                try:
                    id = int(input("Enter ID of expense to delete: "))
                    if id in [expense.id for expense in expense_manager.expenses]:
                        expense_manager.delete_expense(id)
                        print("\nExpense deleted successfully")
                        break
                    print(f"No expense found with ID {id}")
                except ValueError:
                    print("Please enter a valid number.")
            input("\nPress Enter to continue...")

        elif choice == "5":
            clear_terminal()
            if not expense_manager.expenses:
                print("No expenses to update.")
                input("\nPress Enter to continue...")
                continue
            
            print("Current Expenses:\n")
            expense_manager.list_expenses()
            print()
            
            while True:
                try:
                    id = int(input("Enter ID of expense to update: "))
                    if id not in [expense.id for expense in expense_manager.expenses]:
                        print(f"No expense found with ID {id}")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
            
            print("\nLeave blank to keep current value")
            description = input("Enter new description (or press Enter to skip): ").strip()
            description = description if description else None
            
            amount = None
            amount_input = input("Enter new amount (or press Enter to skip): ").strip()
            if amount_input:
                try:
                    amount = float(amount_input)
                    if amount <= 0:
                        print("Amount must be greater than zero.")
                        input("\nPress Enter to continue...")
                        continue
                except ValueError:
                    print("Invalid amount entered.")
                    input("\nPress Enter to continue...")
                    continue
            
            if description is None and amount is None:
                print("No changes provided.")
            else:
                expense_manager.update_expense(id, amount, description)
                print("\nExpense updated successfully")
            input("\nPress Enter to continue...")
        
        elif choice == "6":
            clear_terminal()
            total = sum(float(expense.amount) for expense in expense_manager.expenses)
            print(f"\nTotal expenses: ${total:.2f}")
            input("\nPress Enter to continue...")
        
        elif choice == "7":
            clear_terminal()
            print("Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")
            input("\nPress Enter to continue...")

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

    # Update command
    update_parser = subparsers.add_parser('update', help='Update an expense')
    update_parser.add_argument('--id', type=int, required=True, help='ID of the expense to update')
    update_parser.add_argument('--amount', type=float, help='New amount')
    update_parser.add_argument('--description', help='New description')

    args = parser.parse_args()
    
    expense_manager = Expense_manager('expenses.json')
    print(f'Current local time is: {datetime.now().isoformat()}')

    if not args.command:
        interactive_mode(expense_manager)
        return

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
