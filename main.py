import pandas as pd
from openpyxl import load_workbook

#csv file
file = f"Test.csv"

# Load the CSV file into a DataFrame
df = pd.read_csv("Test.csv")

# Specify the columns you want to read
cols_to_read = ['Post Date', 'Description', 'Debit', 'Credit']  # Added 'Credit'

# Load the CSV file into a DataFrame
df = pd.read_csv(file, usecols=cols_to_read)

# Rename the columns
df = df.rename(columns={'Post Date': 'date', 'Description': 'Description', 'Debit': 'Amount', 'Credit': 'Credit'})  # Added 'Credit'

# Convert the 'date' column to string type
df['date'] = df['date'].astype(str)

# Create a mask where '2023' is in the 'date' column
mask = df['date'].str.contains('2023')

# Use the mask to filter the DataFrame
df = df[mask]

expense_types = {
    'advertising_promotion_social': [],
    'auto_expenses': [],
    'bank_charges': [],
    'charitabel_contributions': [],
    'cable_tvfees_reseatchtools': [],
    'computer_internet': ['COMCAST CABLE COMMUNIC800-COMCASTFL', 'COMCAST'],
    'computer': ['CORSAIR', 'computer', 'Antec', 'PrimoChill', 'LianLi', 'ThermalTake'],
    'dry_cleaning': ['oxiclean'],
    'dues_subscription': ['AAPL','APPLE.COM', 'INTUIT', 'ADOBE SYSTEMS','Rocket Money'],
    'gifts': [],
    'equipment_gym':[ 'gym', 'barbell','dumbells','bench','squat','squat rack','squatrack','squat stand','squatstand','squat stand' , 'squat', 'rack','weights', 'weight', 'mma','mats', 'mat'],
    'gymrent_fitness_memberships': ['ABC*30610-ATHLETICA HEBOCA RATONFL', 'AMERICAN TOP TEAMCOCONUT CREEKFL','30610 ATHLETICA HEALTHBOCA RATONFL','AVIV JIU JITSUBOYNTON BEACHFL', 'AVIV'],
    'home_office_expenses': ['power strip' ,'surge protector'],
    'home_supplies': [],
    'immigration_visa': ['VISA', 'USICS'],
    'interest': ['interest', 'Interest','Interest Earned'],
    'insurance': [],
    'license_and_atheltic_fees': [],
    'labor': [],
    'corners': [],
    'coaches': [],
    'manager_comission': ['Matt Aptaker', 'AOQ', 'AOQ LLC', 'AOQ, LLC', 'AOQ,LLC', 'AOQ LLC.'],
    'massage': [],
    'trainers': [],
    'meals_grocercies': ['publix', 'walmart', 'target', 'costco','Aldi', 'wholefoods'],
    'meals': [],
    'meals_intown': [],
    'medical_family': [],
    'medical_insurance': [],
    'medicals_fight': ['KHEALTH', 'K HEALTH', 'K-HEALTH', 'K HEALTH INC', 'K-HEALTH INC', 'K HEALTH INC.', 'EYE', 'HOWARD', 'HOWARD J GELB', 'WEST BOCA EYE CENTER', 'ELITE IMAGING', 'CVS', 'WALGREENS'],
    'miscellaneous': [],
    'office_supplies': ['STAPLES', 'OFFICE DEPOT', 'OFFICE MAX'],
    'parking_tolls': ['SUNPASS', 'SUNPASS TOLL', 'SUNPASS TOLL REPLENISHMENT', 'SUNPASS','PARKING'],
    'payroll_wages': ['WAGES', 'WAGE'],
    'payroll_taxes': ['tax'],
    'postage_delivery': [],
    'professional_fees': ['Brad', 'CPA4MMA', 'BRAD SMCUKLER'],
    'rent_expenses': [],
    'Repairs_and_Maintenance': [],
    'Retirement_savings': [],
    'Supplements_Nutrition': ['WHEY','VITAMIN','VITAMINS','SUPPLEMENT','SUPPLEMENTS','PROTEIN','PROTEINS'],
    'Supplies_gear_clothing': ['venum','wraps','gloves', 'muay thai', 'jiu jitsu', 'kicking', 'excercise', 'fairtex', 'swimming', 'speedo', 'ASICS'],
    'Taxes_State_IRS_and_other_foreign_taxes': [],
    'Taxes_DMV': [],
    'Telephone': ['T-MOBILE', 'TMOBILE'],
    'Training_expenses': ['AMERICAN TOP TEAMCOCONUT CREEKFL', 'AVIV JIU JITSUBOYNTON BEACHFL', 'AVIV'],
    'Travel_Expense': [],
    'Travel_Airfare': ['UNITED AIRLINES', 'ALASAK AIRLINES ' ,'United' , 'Alaska'],
    'Travel_Hotel': [],
    'Travel_car_rental': [],
    'Travel_uber_lyft': ['UBER', 'UBER *TRIP', 'Uber' , 'Uber *Trip' ,'Lyft' , 'Lyft *Ride'],
    'utilities': [ 'utilities', 'HOA','Deerfield Utilities Beach'],
    'gas': ['CHEVRON', 'WAWA', 'SHELL', 'EXXON', 'RACETRAC'],
    'mortage': ['Mortgage Payment', 'Mortgage','Mr. Cooper'],
    'credit_card':['CREDIT CARD PAYMENT'],
    'zelle':['ZELLE'],
    'debit':['DEBIT'],
    'adp_fee:':['fee'],
    'fund_transfer':['transfer'],
    'electricity':['florida power and light','FPL','Florida'],
    'car_payment':['FORD']
}

try:
 # Function to get expense type
    def get_expense_type(description):
        description = description.lower()  # Convert description to lowercase
        for expense_type, keywords in expense_types.items():
            for keyword in keywords:
                if keyword.lower() in description:  # Convert keyword to lowercase
                    return expense_type
        return 'Other'


    # Apply the get_expense_type function to each row in the DataFrame
    df['expense_type'] = df['Description'].apply(get_expense_type)

    # Define the name of the new sheet
    new_sheet_name = 'Test'  # replace with your actual sheet name

    # Write the DataFrame to a new sheet in the Excel file
    with pd.ExcelWriter('Expense.xlsx', engine='openpyxl', mode='a') as writer:
        df.to_excel(writer, sheet_name=new_sheet_name, index=False)

    print("Operation succeeded")
    
except:
    print("An error occurred")
