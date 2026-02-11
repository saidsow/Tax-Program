import streamlit as st
import pandas as pd

# Define initial expense categories and keywords
categories = {
    'advertising_promotion_social': [],
    'auto_expenses': [],
    'bank_charges': [],
    'charitabel_contributions': [],
    'cable_tvfees_reseatchtools': [],
    'computer_internet': ['COMCAST CABLE COMMUNIC800-COMCASTFL', 'COMCAST'],
    'computer': ['CORSAIR', 'computer', 'Antec', 'PrimoChill', 'LianLi', 'ThermalTake', 'EKWB', 'ASUS.COM', 'ASUS', 'ASUS STORE'],
    'dry_cleaning': ['oxiclean'],
    'dues_subscription': ['AAPL', 'APPLE.COM', 'INTUIT', 'ADOBE SYSTEMS', 'Rocket Money'],
    'gifts': [],
    'equipment_gym': ['gym', 'barbell', 'dumbells', 'bench', 'squat', 'squat rack', 'squatrack', 'squat stand', 'squatstand', 'squat stand', 'squat', 'rack', 'weights', 'weight', 'mma', 'mats', 'mat'],
    'gymrent_fitness_memberships': ['ABC*30610-ATHLETICA HEBOCA RATONFL', 'AMERICAN TOP TEAMCOCONUT CREEKFL', '30610 ATHLETICA HEALTHBOCA RATONFL', 'AVIV JIU JITSUBOYNTON BEACHFL', 'AVIV'],
    'home_office_expenses': ['power strip', 'surge protector'],
    'home_supplies': [],
    'immigration_visa': ['VISA', 'USICS'],
    'interest': ['interest', 'Interest', 'Interest Earned'],
    'insurance': [],
    'license_and_atheltic_fees': [],
    'labor': [],
    'corners': [],
    'coaches': [],
    'manager_comission': ['Matt Aptaker', 'AOQ', 'AOQ LLC', 'AOQ, LLC', 'AOQ,LLC', 'AOQ LLC.'],
    'massage': [],
    'trainers': [],
    'meals_grocercies': ['publix', 'walmart', 'target', 'costco', 'Aldi', 'wholefoods'],
    'meals': [],
    'meals_intown': [],
    'medical_family': [],
    'medical_insurance': [],
    'medicals_fight': ['KHEALTH', 'K HEALTH', 'K-HEALTH', 'K HEALTH INC', 'K-HEALTH INC', 'K HEALTH INC.', 'EYE', 'HOWARD', 'HOWARD J GELB', 'WEST BOCA EYE CENTER', 'ELITE IMAGING', 'CVS', 'WALGREENS'],
    'miscellaneous': [],
    'office_supplies': ['STAPLES', 'OFFICE DEPOT', 'OFFICE MAX'],
    'parking_tolls': ['SUNPASS', 'SUNPASS TOLL', 'SUNPASS TOLL REPLENISHMENT', 'SUNPASS', 'PARKING'],
    'payroll_wages': [],
    'payroll_taxes': [],
    'postage_delivery': [],
    'professional_fees': ['Brad', 'CPA4MMA', 'BRAD SMCUKLER'],
    'rent_expenses': [],
    'Repairs_and_Maintenance': [],
    'Retirement_savings': [],
    'Supplements_Nutrition': ['WHEY', 'VITAMIN', 'VITAMINS', 'SUPPLEMENT', 'SUPPLEMENTS', 'PROTEIN', 'PROTEINS'],
    'Supplies_gear_clothing': ['venum', 'wraps', 'gloves', 'muay thai', 'jiu jitsu', 'kicking', 'excercise', 'fairtex', 'swimming', 'speedo', 'ASICS'],
    'Taxes_State_IRS_and_other_foreign_taxes': [],
    'Taxes_DMV': [],
    'Telephone': ['T-MOBILE', 'TMOBILE'],
    'Training_expenses': ['AMERICAN TOP TEAMCOCONUT CREEKFL', 'AVIV JIU JITSUBOYNTON BEACHFL', 'AVIV'],
    'Travel_Expense': [],
    'Travel_Airfare': ['UNITED AIRLINES', 'ALASAK AIRLINES ', 'United', 'Alaska'],
    'Travel_Hotel': [],
    'Travel_car_rental': [],
    'Travel_uber_lyft': ['UBER', 'UBER *TRIP', 'Uber', 'Uber *Trip', 'Lyft', 'Lyft *Ride'],
    'utilities': ['FPL', 'utilities', 'HOA', 'Deerfield Utilities Beach'],
    'gas': ['CHEVRON', 'WAWA', 'SHELL', 'EXXON', 'RACETRAC'],
    'mortage': ['Mortgage Payment', 'Mortgage'],
    'credit_card': ['CREDIT CARD PAYMENT'],
    'zelle': ['ZELLE'],
    'credit': ['CREDIT', 'PYMT', 'ACH'],
    'debit': ['DEBIT'],
    'taxes': ['TAXES']
}

# Function to categorize expenses
def categorize_expenses(description):
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword.lower() in description.lower():
                return category
    return 'Not an Expense'

# Function to process the uploaded CSV file
def process_csv(file):
    df = pd.read_csv(file)
    df['Category'] = df['Description'].apply(categorize_expenses)
    return df

# Function to export results to Excel with a separate sheet for all expenses
def export_to_excel(dataframes, output_path):
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        all_expenses = pd.DataFrame()
        for name, df in dataframes.items():
            df.to_excel(writer, sheet_name=name, index=False)
            expenses = df[df['Category'] != 'Not an Expense']
            all_expenses = pd.concat([all_expenses, expenses], ignore_index=True)
        if not all_expenses.empty:
            all_expenses.to_excel(writer, sheet_name='All Expenses', index=False)

# Streamlit UI
st.set_page_config(page_title="Expense Categorization App", layout="wide")

# Add a header with a description
st.markdown("""
    <div style="display:flex; justify-content: space-between; align-items: center;">
        <h1>Expense Categorization App</h1>
        <p>By Said Sowma</p>
    </div>
    <hr>
    <p>This app allows you to upload CSV files containing transaction data, categorize the expenses based on the description, and export the categorized data to an Excel file. You can alos add categories and keywords on the right to customize it to your needs.</p>
""", unsafe_allow_html=True)

# Sidebar for adding categories and keywords
st.sidebar.header("Add New Category")
new_category = st.sidebar.text_input("Category Name")
add_category = st.sidebar.button("Add Category")
if add_category and new_category:
    if new_category not in categories:
        categories[new_category] = []
        st.sidebar.success(f"Category '{new_category}' added.")

st.sidebar.header("Add Keywords to Category")
category = st.sidebar.selectbox("Select Category", list(categories.keys()))
new_keyword = st.sidebar.text_input("Keyword")
add_keyword = st.sidebar.button("Add Keyword")
if add_keyword and new_keyword:
    if new_keyword not in categories[category]:
        categories[category].append(new_keyword)
        st.sidebar.success(f"Keyword '{new_keyword}' added to category '{category}'.")

# File uploader
uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True, type=['csv'])

# Processing and displaying the uploaded files
if uploaded_files:
    dataframes = {}
    for uploaded_file in uploaded_files:
        df = process_csv(uploaded_file)
        dataframes[uploaded_file.name] = df
        st.write(f"Processed {uploaded_file.name}")
        st.dataframe(df)

    if st.button("Export to Excel"):
        output_path = "categorized_expenses.xlsx"
        export_to_excel(dataframes, output_path)
        st.success(f"Exported to {output_path}")
        st.download_button(label="Download Excel file", data=open(output_path, 'rb').read(), file_name=output_path, mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
