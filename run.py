import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('MySavingGoal')


def update_savings():
    """
    Updates the savings sheet with the latest expenses and incomes
    """
    incomes_sheet = SHEET.worksheet("Incomes")
    expenses_sheet = SHEET.worksheet("Expenses")
    savings_sheet = SHEET.worksheet("Savings")

    incomes = incomes_sheet.col_values(4)[1:]
    total_income = sum(map(float, incomes))
    print(f"Total up to date incomes are {total_income} €\n")

    expenses = expenses_sheet.col_values(4)[1:]
    total_expense = sum(map(float, expenses))
    print(f"Total up to date expenses are {total_expense} €\n")

    current_savings = total_income - total_expense
    date = datetime.now().strftime('%d/%m/%Y')
    print(f"Your current savings are {current_savings} €\n")
    print("Updating the savings sheet...")
    savings_sheet.append_row([
        date, datetime.now().isocalendar()[1], current_savings])


def add_new_income():
    """
    Prompts the user to input new incomes and adds them to the Incomes sheet
    until the user decides to stop.
    """
    incomes_sheet = SHEET.worksheet("Incomes")

    while True:
        while True:
            date = input("Enter the date of the income (dd/mm/yyyy): ")
            try:
                datetime.strptime(date, '%d/%m/%Y')
                break
            except ValueError:
                print("Invalid date format. Please try again.")

        income_types = ["Wages", "Freelance", "Investment", "Other"]
        print("Select the type of income:")
        for idx, income_type in enumerate(income_types, start=1):
            print(f"{idx}. {income_type}")

        while True:
            try:
                income_type_choice = int(
                    input("Enter the number correspondingto the income type: ")
                    )
                if 1 <= income_type_choice <= len(income_types):
                    income_type = income_types[income_type_choice - 1]
                    break
                else:
                    print(
                        "Invalid choice. Please choose a number from the list."
                        )
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            amount = input("Enter the amount of income (€): ")
            try:
                amount = float(amount)
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")

        week_number = datetime.strptime(date, '%d/%m/%Y').isocalendar()[1]

        incomes_sheet.append_row([date, week_number, income_type, amount])
        print("New income added successfully!\n")

        while True:
            more_incomes = input(
                "Do you want to add another income? (yes/no): "
                ).strip().lower()
            if more_incomes == 'yes':
                add_new_income()
                break
            elif more_incomes == 'no':
                break
            else:
                print("Invalid input, please type 'yes' or 'no'.")


def add_new_expenses():
    """
    Prompts the user to input new expenses and adds them to the Expenses sheet
    until the user decides to stop.
    """
    expenses_sheet = SHEET.worksheet("Expenses")

    while True:
        while True:
            date = input("Enter the date of the expense (dd/mm/yyyy): ")
            try:
                datetime.strptime(date, '%d/%m/%Y')
                break
            except ValueError:
                print("Invalid date format. Please try again.")

        expenses_types = [
            "Housing", "Transport", "Food", "Cosmetics", "Health & Wellness",
            "Entertainment & Leisure", "Clothing & Personal Care", "Gifts"
            ]
        print("Select the type of expenses:")
        for idx, expenses_type in enumerate(expenses_types, start=1):
            print(f"{idx}. {expenses_type}")

        while True:
            try:
                expenses_type_choice = int(input(
                    "Enter the number corresponding to the expenses type: "))
                if 1 <= expenses_type_choice <= len(expenses_types):
                    expenses_type = expenses_types[expenses_type_choice - 1]
                    break
                else:
                    print(
                        "Invalid choice. Please choose a number from the list."
                        )
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            amount = input("Enter the amount of expenses (€): ")
            try:
                amount = float(amount)
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")

        week_number = datetime.strptime(date, '%d/%m/%Y').isocalendar()[1]

        expenses_sheet.append_row([date, week_number, expenses_type, amount])
        print("New expense added successfully!\n")

        while True:
            more_expenses = input(
                "Do you want to add another expenses? (yes/no): "
                ).strip().lower()
            if more_expenses == 'yes':
                break
            elif more_expenses == 'no':
                print("No more expenses to add.\n")
                return
            else:
                print("Invalid input, please type 'yes' or 'no'.")


def calculate_goal_progress():
    """
    Calculates how much is still missing from the savings goal and
    how much needs to be saved per week on average to reach the goal.
    """
    savings_sheet = SHEET.worksheet("Savings")
    goal_sheet = SHEET.worksheet("Goal")

    last_row = len(savings_sheet.col_values(1))
    current_savings = float(savings_sheet.cell(last_row, 3).value)
    goal_data = goal_sheet.row_values(2)
    goal_date_str = goal_data[0]
    goal_amount = float(goal_data[2])

    goal_date = datetime.strptime(goal_date_str, '%d/%m/%Y')

    missing_amount = goal_amount - current_savings

    current_date = datetime.now()
    remaining_weeks = (goal_date - current_date).days // 7

    if remaining_weeks > 0:
        weekly_savings_needed = missing_amount / remaining_weeks
    else:
        weekly_savings_needed = missing_amount

    print(f"You still need to save {missing_amount:.2f} € to "
          f"reach your goal of {goal_amount} € by "
          f"{goal_date_str}.")

    if remaining_weeks > 0:
        print(f"You have {remaining_weeks} weeks remaining.")
        print(f"On average, you need to save {weekly_savings_needed:.2f} € "
              f"per week to reach your goal.")
    else:
        print("The goal date has passed. You need to save the remaining "
              "amount immediately.")


def main():
    while True:
        add_income_prompt = input(
            "Do you want to add any new incomes? (yes/no): "
            ).strip().lower()
        if add_income_prompt == "yes":
            add_new_income()
            break
        elif add_income_prompt == "no":
            break
        else:
            print("Invalid input, please type 'yes' or 'no'.")

    while True:
        add_expenses_prompt = input(
            "Do you want to add any new expenses? (yes/no): "
            ).strip().lower()
        if add_expenses_prompt == "yes":
            add_new_expenses()
            break
        elif add_expenses_prompt == "no":
            break
        else:
            print("Invalid input, please type 'yes' or 'no'.")

    update_savings()
    calculate_goal_progress()


main()
