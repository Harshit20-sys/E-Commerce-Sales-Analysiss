import pandas as pd
import os

# ===============================
# Project Paths
# ===============================

RAW_PATH = "../01_data/01_Raw"
CLEANED_PATH = "../01_data/02_Cleaned"

os.makedirs(CLEANED_PATH, exist_ok=True)

# ===============================
# CSV Files
# ===============================

files = [
    "olist_customers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv"
]

print("=" * 70)
print("      OLIST E-COMMERCE DATA CLEANING REPORT")
print("=" * 70)

# ===============================
# Loop through all files
# ===============================

for file in files:

    print("\n" + "=" * 70)
    print(f"FILE : {file}")
    print("=" * 70)

    df = pd.read_csv(os.path.join(RAW_PATH, file))

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nMissing Values")
    print(df.isnull().sum())

    duplicates = df.duplicated().sum()
    print(f"\nDuplicate Rows : {duplicates}")

    print("\nData Types")
    print(df.dtypes)

    df.to_csv(
        os.path.join(CLEANED_PATH, file),
        index=False
    )

print("\n")
print("=" * 70)
print("ALL FILES CHECKED SUCCESSFULLY")
print("Cleaned files saved in data/cleaned/")
print("=" * 70)