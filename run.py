import gspread
from google.oauth2 import service_account

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = service_account.Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

def get_sales_data():
    """
    Get sales figures input from the user.
    """
    print("please enter details from last market")
    print("data should be six numbers")
    print("Example: 1, 2, 3\n")

    data_str = input("Enter data here: ")
    print(f"The data provided is {data_str}")

    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    try: 
        if len(values) != 3:
            raise ValueError(f"Stupid you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")

get_sales_data()