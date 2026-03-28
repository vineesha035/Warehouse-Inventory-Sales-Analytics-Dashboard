import kagglehub
import pandas as pd

# Step 1: Download dataset from Kaggle
dataset_path = kagglehub.dataset_download("salahuddinahmedshuvo/grocery-inventory-and-sales-dataset")
csv_file = f"{dataset_path}/grocery_inventory_sales.csv"  

# Step 2: Load dataset into Pandas DataFrame
df = pd.read_csv(csv_file)
print(" Dataset Loaded")

# Step 3: Inspect Data Types Before Cleaning
print(" Data Types Before Cleaning:\n", df.dtypes)

# Step 4: Convert Date Columns to Proper DateTime Format
date_columns = ['Date_Received', 'Last_Order_Date', 'Expiration_Date']
for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')  # Convert with error handling
    print(f" Converted {col} to datetime format.")

# Step 5: Convert Unit_Price to Numeric (Remove $ and Convert)

df['Unit_Price'] = df['Unit_Price'].replace('[\$,]', '', regex=True)  # Remove $ signs
df['Unit_Price'] = pd.to_numeric(df['Unit_Price'], errors='coerce')  # Convert to numeric
print(" Unit_Price conversion complete.")

# Step 6: Handling Missing Values

df.fillna({
    'Stock_Quantity': 0,  # If stock is missing, assume 0
    'Reorder_Level': df['Reorder_Level'].median(),  # Fill with median reorder level
    'Reorder_Quantity': df['Reorder_Quantity'].median(),  # Fill missing reorder quantity
}, inplace=True)

# Step 7: Remove Duplicates

df.drop_duplicates(inplace=True)

# Step 8: Verify the Cleaning Process

print("\n Data Types After Cleaning:\n", df.dtypes)
print("\n Missing Values After Cleaning:\n", df.isnull().sum())

# Step 9: Save Processed Data for Tableau

cleaned_file = "inventory_data_cleaned.csv"
df.to_csv(cleaned_file, index=False)
print(f" Cleaned dataset saved as {cleaned_file}")


