import streamlit as st

# Streamlit UI configuration
st.set_page_config(page_title="Athlete's Tax Calculator", layout="centered")

# Sidebar for navigation
st.sidebar.title("Navigation")
sections = ["Income", "Expenses", "Tax Calculation", "Reports"]
selected_section = st.sidebar.radio("Go to", sections)

# Main content based on selected section
if selected_section == "Income":
    st.header("Income Section")
    st.write("This is where you'll input your income details.")

elif selected_section == "Expenses":
    st.header("Expenses Section")
    st.write("This is where you'll input your expenses details.")

elif selected_section == "Tax Calculation":
    st.header("Tax Calculation Section")
    st.write("This is where the tax calculations will be displayed.")

elif selected_section == "Reports":
    st.header("Reports Section")
    st.write("This is where you can generate and view reports.")


# Income sources input section
income_sources = {
    "Salary/Wages": 0.0,
    "Endorsements/Sponsorships": 0.0,
    "Prize Money": 0.0,
    "Appearance Fees": 0.0,
    "Bonuses": 0.0,
    "Merchandise Sales": 0.0,
    "Other Income": 0.0
}

# Function to display income input fields
def display_income_fields(income_sources):
    total_income = 0.0
    for source, amount in income_sources.items():
        income_sources[source] = st.number_input(f"{source} ($)", min_value=0.0, value=amount)
        total_income += income_sources[source]
    return total_income

# Section to handle income input
if selected_section == "Income":
    st.header("Income Sources")

    # Display predefined income fields
    total_income = display_income_fields(income_sources)

    # Placeholder for new income sources
    new_income_sources = {}

    # Input fields to add new income source
    st.subheader("Add New Income Source")
    new_income_name = st.text_input("Income Source Name")
    new_income_amount = st.number_input("Income Amount ($)", min_value=0.0, value=0.0)
    if st.button("Add Income Source"):
        if new_income_name and new_income_amount > 0:
            new_income_sources[new_income_name] = new_income_amount

    # Display newly added income sources
    total_income += display_income_fields(new_income_sources)

    # Display total income
    st.subheader("Total Income")
    st.write(f"Your total annual income is: ${total_income:.2f}")


