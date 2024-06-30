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
        print("please enter details from last market")
        print("data should be six numbers")
        print("Example: 1, 2, 3\n")

        data_str = input("Enter data here: ")
        print(f"The data provided is {data_str}")

        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
           print("Data is valid")
           break
        
        
        
    

def validate_data(values):
    print(values)
    try:
        [int(value) for value in values] 
        if len(values) != 6:
            raise ValueError(f"Stupid you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
        return False
    
    return True

def update_sales_worksheet(data):
    """
    Updates sales
    """
    print("updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("sales worksheet updated sucessfully \n")

data = get_sales_data() 

sales_data = [int(num) for num in data]
update_sales_worksheet(sales_data)