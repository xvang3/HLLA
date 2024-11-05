import pandas as pd

# Define the base URL for raw GitHub content
base_github_url = "https://raw.githubusercontent.com/xvang3/HLLA/sqlite-testing/hmoob_lus/media/"

# Load the Excel file
file_path = "PDF HLLA.xlsx"  # Update this with the path to your Excel file
df = pd.read_excel(file_path)

# Columns to update
audio_columns = ["Male Audio", "Female Audio", "Pronunciation Video", "Real Video", "Animated Video"]

# Iterate through each specified column and update the URLs
for column in audio_columns:
    if column in df.columns:  # Only process if the column exists
        df[column] = df[column].apply(lambda x: base_github_url + x.split('/')[-1] if pd.notna(x) else x)

# Save the updated DataFrame back to an Excel file
output_file_path = "updated PDF HLLA.xlsx"  # Specify where you want to save the updated file
df.to_excel(output_file_path, index=False)

print("Excel file has been updated with GitHub raw URLs.")
