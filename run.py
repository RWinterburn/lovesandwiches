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
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 1, 2, 3, 4, 5, 6\n")

        data_str = input("Enter data here: ")
        print(f"The data provided is {data_str}")

        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print("Data is valid")
            return [int(num) for num in sales_data]  # Ensure data is converted to integers

def validate_data(values):
    """
    Validate the sales data input by the user.
    """
    print(values)
    try:
        # Ensure all values can be converted to integers
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(f"Expected 6 values, but got {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")
        return False
    
    return True

def update_sales_worksheet(data):
    """
    Update sales worksheet with new data.
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)  # Data is already in integer format
    print("Sales worksheet updated successfully.\n")

# Get data from the user and update the worksheet
data = get_sales_data() 
sales_data = [int(num) for num in data]
update_sales_worksheet(sales_data)
