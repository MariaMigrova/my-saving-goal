import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('MySavingGoal')


def update_goal():
    """
    Checks with the user if he/she wants to update their goal
    and overwrites the goal in the spreadsheet if confirmed.
    """
    goal_sheet = SHEET.worksheet("Goal")
    date = goal_sheet.col_values(1)[1]
    goal_amount = goal_sheet.col_values(3)[1]

    print(f"Your current goal is to save {goal_amount} € by {date}.")

    while True:
        goal_change = input(
            "Do you want to make changes to this goal? ('yes'/'no'):\n"
        ).strip().lower()

        if goal_change == "yes":
            while True:
                while True:
                    new_goal_amount = input("New savings goal amount (€):\n")
                    try:
                        new_goal_amount = float(new_goal_amount)
                        break
                    except ValueError:
                        print("Invalid amount. Please enter a number.")

                while True:
                    new_goal_date = input(
                        "New savings goal date: (dd/mm/yyyy):\n")
                    try:
                        new_goal_date_obj = datetime.strptime(
                            new_goal_date, '%d/%m/%Y')
                        today = datetime.today()
                        if new_goal_date_obj < today:
                            print(
                                "Your saving goal date cannot be in the past. "
                                "Please try again.")
                        else:
                            new_goal_date = new_goal_date_obj.strftime(
                                "%d/%m/%Y")
                            break
                    except ValueError:
                        print("Invalid date format. Please try again.")

                while True:
                    confirm_update = input(
                        f"New goal: Save {new_goal_amount} €\n"
                        f"by {new_goal_date}.\n"
                        "Are you happy with this update? ('yes'/'no'):\n"
                    ).strip().lower()

                    if confirm_update == "yes":
                        goal_sheet.update(
                            range_name='A2', values=[[new_goal_date]])
                        goal_sheet.update(
                            range_name='C2', values=[[new_goal_amount]])

                        week_number = datetime.strptime(
                            new_goal_date, '%d/%m/%Y').isocalendar()[1]
                        goal_sheet.update(
                            range_name='B2', values=[[week_number]])

                        print("Goal updated successfully!")
                        return

                    elif confirm_update == "no":
                        print("Let's try updating the goal again.")
                        break

                    else:
                        print("Invalid input, please type 'yes' or 'no'.")

        elif goal_change == "no":
            print("No changes made to your savings goal.")
            break
        else:
            print("Invalid input, please type 'yes' or 'no'.")


def update_savings():
    """
    Updates the savings sheet with the latest expenses and incomes
    """
    incomes_sheet = SHEET.worksheet("Incomes")
    expenses_sheet = SHEET.worksheet("Expenses")
    savings_sheet = SHEET.worksheet("Savings")

    incomes = incomes_sheet.col_values(4)[1:]
    total_income = sum(map(float, incomes))
    expenses = expenses_sheet.col_values(4)[1:]
    total_expense = sum(map(float, expenses))
    current_savings = total_income - total_expense
    date = datetime.now().strftime('%d/%m/%Y')

    print("\n===============================")
    print("        SAVINGS SUMMARY         ")
    print("===============================\n")
    print(f"Total Income:    {total_income:.2f} €")
    print(f"Total Expenses:  {total_expense:.2f} €")
    print(f"Current Savings: {current_savings:.2f} €\n")
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
            saving_date = input("Enter the date of the income (dd/mm/yyyy):\n")
            try:
                saving_date_obj = datetime.strptime(saving_date, '%d/%m/%Y')
                today = datetime.today()
                three_months_earlier = today - timedelta(days=90)

                if saving_date_obj > today:
                    print(
                        "Your saving date cannot be in the future. "
                        "Please try again.")
                elif saving_date_obj < three_months_earlier:
                    print(
                        "Your saving date cannot be older than 3 months. "
                        "Please try again.")
                else:
                    saving_date = saving_date_obj.strftime("%d/%m/%Y")
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
                    input(
                        "Enter the number corresponding to the income type:\n")
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
            amount = input("Enter the amount of income (€):\n")
            try:
                amount = float(amount)
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")

        week_number = datetime.strptime(
            saving_date, '%d/%m/%Y').isocalendar()[1]

        while True:
            check = input(
                f"Date: {saving_date}\n"
                f"Income type: {income_type}\n"
                f"Amount: {amount}\n"
                "Do you want to save this? ('yes'/'no'): ")
            if check == "yes":
                incomes_sheet.append_row(
                    [saving_date, week_number, income_type, amount])
                print("New income added successfully!\n")
                break
            elif check == "no":
                print("Income entry discarded. Please re-enter details.\n")
                break
            else:
                print("Invalid input, please type 'yes' or 'no'.")

        while True:
            more_incomes = input(
                "Do you want to add another income? (yes/no):\n"
                ).strip().lower()
            if more_incomes == 'yes':
                break
            elif more_incomes == 'no':
                return
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
            expense_date = input(
                "Enter the date of the expense (dd/mm/yyyy):\n")
            try:
                expense_date_obj = datetime.strptime(expense_date, '%d/%m/%Y')
                today = datetime.today()
                three_months_earlier = today - timedelta(days=90)

                if expense_date_obj > today:
                    print(
                        "Your expense date cannot be in the future. "
                        "Please try again.")
                elif expense_date_obj < three_months_earlier:
                    print(
                        "Your expense date cannot be older than 3 months. "
                        "Please, try again.")
                else:
                    expense_date = expense_date_obj.strftime("%d/%m/%Y")
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
                    "Enter the number corresponding to the expenses type:\n"))
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
            amount = input("Enter the amount of expenses (€):\n")
            try:
                amount = float(amount)
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")

        week_number = datetime.strptime(
            expense_date, '%d/%m/%Y').isocalendar()[1]

        while True:
            check = input(
                f"Date: {expense_date}\n"
                f"Expenses type: {expenses_type}\n"
                f"Amount: {amount}\n"
                "Do you want to save this? ('yes'/'no'): ")
            if check == "yes":
                expenses_sheet.append_row(
                    [expense_date, week_number, expenses_type, amount])
                print("New expenses added successfully!\n")
                break
            elif check == "no":
                print("Expense entry discarded. Please re-enter details.\n")
                break
            else:
                print("Invalid input, please type 'yes' or 'no'.")

        while True:
            more_expenses = input(
                "Do you want to add another expenses? (yes/no):\n"
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

    print("\n===============================")
    print("       GOAL PROGRESS REPORT     ")
    print("===============================\n")
    print(f"Goal Amount:       {goal_amount:.2f} €")
    print(f"Current Savings:   {current_savings:.2f} €")
    print(f"Amount Remaining:  {missing_amount:.2f} €")

    if remaining_weeks > 0:
        weekly_savings_needed = missing_amount / remaining_weeks
        print(f"Weeks Remaining:   {remaining_weeks}")
        print(f"Average Weekly Savings Needed: {weekly_savings_needed:.2f} €")
    else:
        print(
            "The goal date has passed.",
            "You need to save the remaining amount immediately.\n")


def main():
    print("\n===============================")
    print("       WELCOME TO FINANCE APP   ")
    print("===============================\n")

    update_goal()

    while True:
        print("~~~INCOMES~~~")
        add_income_prompt = input(
            "Do you want to add any new incomes? (yes/no):\n"
            ).strip().lower()
        if add_income_prompt == "yes":
            add_new_income()
            break
        elif add_income_prompt == "no":
            break
        else:
            print("Invalid input, please type 'yes' or 'no'.")

    while True:
        print("~~~EXPENSES~~~")
        add_expenses_prompt = input(
            "Do you want to add any new expenses? (yes/no):\n"
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

    print("\n===============================")
    print("       THANK YOU FOR USING      ")
    print("          FINANCE APP           ")
    print("===============================\n")


main()
