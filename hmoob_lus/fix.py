import pandas as pd

# Load the Excel file
df = pd.read_excel("PDF HLLA.xlsx")

# Define columns that need media URL adjustments
media_columns = ["Male Audio", "Female Audio", "Pronunciation Video", "Real Video", "Animated Video"]

# Add MEDIA_URL prefix to relevant columns and replace spaces with %20
for column in media_columns:
    # Check if column exists to avoid errors
    if column in df.columns:
        df[column] = df[column].apply(lambda x: f"/localhost:8000/{x.replace(' ', '%20')}" if pd.notna(x) else x)

# Save the modified Excel file
df.to_excel("modified_excel_file.xlsx", index=False)
