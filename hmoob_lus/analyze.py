import pandas as pd

# Load the Excel file to inspect its content
excel_path = 'C:\\Users\\ntxhw\\Downloads\\PDF HLLA.xlsx'
df_excel = pd.read_excel(excel_path)

# Display the first few rows to understand its structure
df_excel.head()
