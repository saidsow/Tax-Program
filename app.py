import streamlit as st
import pandas as pd
import openpyxl

# Define the expense categories and keywords extracted from the provided files
categories = {
    'Travel': ['flight', 'hotel', 'taxi', 'uber', 'bus', 'train', 'airbnb', 'gas'],
    'Meals': ['restaurant', 'dinner', 'lunch', 'breakfast', 'coffee', 'snacks'],
    'Office Supplies': ['paper', 'pen', 'stapler', 'notebook', 'printer', 'ink', 'envelope'],
    'Software': ['subscription', 'license', 'software', 'saas', 'cloud'],
    'Marketing': ['advertising', 'marketing', 'promotion', 'seo', 'social media'],
    'Utilities': ['electricity', 'water', 'internet', 'phone', 'utility'],
    'Maintenance': ['repair', 'maintenance', 'service', 'cleaning'],
    'Rent': ['rent', 'lease', 'mortgage'],
    'Insurance': ['insurance', 'premium', 'coverage'],
    'Entertainment': ['movie', 'concert', 'show', 'event', 'game'],
    'Miscellaneous': ['misc', 'other', 'sundry'],
    'Professional Services': ['consulting', 'legal', 'accounting', 'freelance'],
    'Travel': ['flight', 'hotel', 'taxi', 'uber', 'bus', 'train', 'airbnb', 'gas'],
    'Meals': ['restaurant', 'dinner', 'lunch', 'breakfast', 'coffee', 'snacks'],
    'Office Supplies': ['paper', 'pen', 'stapler', 'notebook', 'printer', 'ink', 'envelope'],
    'Software': ['subscription', 'license', 'software', 'saas', 'cloud'],
    'Marketing': ['advertising', 'marketing', 'promotion', 'seo', 'social media'],
    'Utilities': ['electricity', 'water', 'internet', 'phone', 'utility'],
    'Maintenance': ['repair', 'maintenance', 'service', 'cleaning'],
    'Rent': ['rent', 'lease', 'mortgage'],
    'Insurance': ['insurance', 'premium', 'coverage'],
    'Entertainment': ['movie', 'concert', 'show', 'event', 'game'],
    'Miscellaneous': ['misc', 'other', 'sundry'],
    'Professional Services': ['consulting', 'legal', 'accounting', 'freelance']
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
st.title('Expense Categorization App')

uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True, type=['csv'])

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
