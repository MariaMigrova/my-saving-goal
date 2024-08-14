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
    savings_sheet.append_row([date, datetime.now().isocalendar()[1], current_savings])

update_savings()
    













