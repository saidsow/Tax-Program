# Expense Categorization App

This app helps you categorize expenses from CSV transaction files and export the results to Excel. It is designed for easy customization, allowing you to add your own categories and keywords for expense classification.

## Features
 - Upload multiple CSV files containing transaction data
 - Automatic categorization of expenses based on description keywords
 - Add new categories and keywords via the sidebar
 - Export categorized results to an Excel file with a summary sheet
 - Built with Streamlit for a simple web interface

## How It Works
1. Upload your CSV files (each should have a `Description` column).
2. The app matches transaction descriptions to categories using predefined and user-added keywords.
3. View categorized results in the app.
4. Export all categorized data to an Excel file, including a summary sheet of all expenses.

## Getting Started

### Prerequisites
 - Python 3.8+
 - pip (Python package manager)

### Installation
1. Clone or download this repository.
2. Install dependencies:
	```bash
	pip install -r requirements.txt
	```

### Running the App
1. Start the Streamlit app:
	```bash
	streamlit run app.py
	```
2. Open the provided local URL in your browser.

### Usage
1. Use the sidebar to add categories and keywords as needed.
2. Upload your CSV files using the uploader.
3. Review categorized results.
4. Click "Export to Excel" to generate and download the Excel file.

## CSV Format
Your CSV files should include at least a `Description` column. Example:

| Date       | Description           | Amount |
|------------|----------------------|--------|
| 2026-01-01 | COMCAST CABLE COMMUNIC800-COMCASTFL | 100.00 |
| 2026-01-02 | UBER *TRIP            | 25.00  |

## License
Proprietary License

This software is proprietary. You may not use, copy, modify, distribute, or sublicense this code without explicit written permission from the author.

## Author
Said Sowma
# TaxStream
 
