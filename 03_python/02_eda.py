import pandas as pd

# Load Dataset
orders = pd.read_csv("../01_data/01_Raw/olist_orders_dataset.csv")
reviews = pd.read_csv("../01_data/01_Raw/olist_order_reviews_dataset.csv")

print("="*60)
print("OLIST ORDERS DATASET")
print("="*60)

# Shape
print("\nDataset Shape:")
print(orders.shape)

# Columns
print("\nColumns:")
print(orders.columns.tolist())

# Data Types
print("\nData Types:")
print(orders.dtypes)

# Missing Values
print("\nMissing Values:")
print(orders.isnull().sum())

# Duplicate Rows
print("\nDuplicate Rows:")
print(orders.duplicated().sum())

# Order Status
print("\nOrder Status Distribution:")
print(orders["order_status"].value_counts())

# ===========================
# Review Score Distribution
# ===========================

review_distribution = (
    reviews["review_score"]
    .value_counts()
    .sort_index()
)

print("\n==============================")
print("REVIEW SCORE DISTRIBUTION")
print("==============================")

print(review_distribution)