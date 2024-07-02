import gspread
from google.oauth2 import service_account
from pprint import pprint

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
    
def update_surplus_worksheet(data):
    """
    Update surplus worksheet with new data.
    """
    print("Updating surplus worksheet...\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)  # Data is already in integer format
    print("Sales worksheet updated successfully.\n")
    
    
    #this code does both the above functions its called refactoring
def update_worksheet(data, worksheet):
    """
    Receives the list of integers to be instered into a worksheet 
    update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")
    
def calculate_surplus_data(sales_row):
    """
    Compare sales and calculate surplus for each item.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data

def get_last_5_entries_sales():
    """
    Collects collumns of data fromsales woreksheet collecting 
    last 5 sandwich entries
    """
    sales = SHEET.worksheet("sales")
   # collumn = sales.col_values()
    #print(collumn)
    # fff
    
    columns = []
    for ind in range(1, 7):
        column =sales.col_values(ind)
        columns.append(column[-5:])
    pprint(columns)

def main():
    """
    Run all programs.
    """
    print("Welcome to Love Sandwiches Data Automation")
    data = get_sales_data()
    update_worksheet(data, "sales")
    # Assuming you want to calculate surplus data after updating sales
    new_surplus_data = calculate_surplus_data(data)
    update_surplus_worksheet(new_surplus_data, "surplus") #refactored code

# Calling the main function to run the program
# main()

get_last_5_entries_sales()
