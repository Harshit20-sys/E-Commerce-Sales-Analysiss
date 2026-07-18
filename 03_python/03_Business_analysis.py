import pandas as pd

# Load datasets
orders = pd.read_csv("../01_data/01_Raw/olist_orders_dataset.csv")
order_items = pd.read_csv("../01_data/01_Raw/olist_order_items_dataset.csv")
products = pd.read_csv("../01_data/01_Raw/olist_products_dataset.csv")
translation = pd.read_csv("../01_data/01_Raw/product_category_name_translation.csv")

print("Orders:", orders.shape)
print("Order Items:", order_items.shape)
print("Products:", products.shape)
print("Translation:", translation.shape)


# ===========================
# Merge Data
# ===========================

# Merge Order Items with Products
merged = order_items.merge(
    products,
    on="product_id",
    how="left"
)

# Merge with Category Translation
merged = merged.merge(
    translation,
    on="product_category_name",
    how="left"
)

print("\nMerged Dataset Shape:")
print(merged.shape)

print("\nColumns:")
print(merged.columns.tolist())


# ===========================
# Revenue by Category
# ===========================

revenue = (
    merged.groupby("product_category_name_english")["price"]
    .sum()
    .sort_values(ascending=False)
)

print("\n==============================")
print("TOP 10 REVENUE CATEGORIES")
print("==============================")

print(revenue.head(10))


# ===========================
# Monthly Sales Analysis
# ===========================

# Convert purchase date to datetime
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"],
    format="%d-%m-%Y %H:%M",
    errors="coerce"
)


# Extract Month-Year
orders["Month"] = orders["order_purchase_timestamp"].dt.to_period("M")

# Merge Orders with Order Items
monthly_sales = orders.merge(
    order_items,
    on="order_id",
    how="inner"
)

# Revenue by Month
monthly_sales = (
    monthly_sales.groupby("Month")["price"]
    .sum()
    .sort_values(ascending=False)
)

print("\n==============================")
print("TOP 10 SALES MONTHS")
print("==============================")

print(monthly_sales.head(10))


# ===========================
# Best Performing Region
# ===========================

customers = pd.read_csv("../01_data/01_Raw/olist_customers_dataset.csv")

# Merge Orders with Customers
region_sales = orders.merge(
    customers,
    on="customer_id",
    how="inner"
)

# Merge with Order Items
region_sales = region_sales.merge(
    order_items,
    on="order_id",
    how="inner"
)

# Revenue by State
state_revenue = (
    region_sales.groupby("customer_state")["price"]
    .sum()
    .sort_values(ascending=False)
)

print("\n==============================")
print("TOP 10 STATES BY REVENUE")
print("==============================")

print(state_revenue.head(10))


# ===========================
# Average Order Value (AOV)
# ===========================

# Revenue per Order
order_value = (
    order_items.groupby("order_id")["price"]
    .sum()
    .reset_index()
)

# Merge with Orders
aov = orders.merge(
    order_value,
    on="order_id",
    how="inner"
)

# Convert Purchase Date
aov["order_purchase_timestamp"] = pd.to_datetime(
    aov["order_purchase_timestamp"],
    dayfirst=True,
    format="mixed"
)

# Extract Month
aov["Month"] = aov["order_purchase_timestamp"].dt.to_period("M")

# Monthly Average Order Value
monthly_aov = (
    aov.groupby("Month")["price"]
    .mean()
    .round(2)
)

print("\n==============================")
print("MONTHLY AVERAGE ORDER VALUE")
print("==============================")

print(monthly_aov)