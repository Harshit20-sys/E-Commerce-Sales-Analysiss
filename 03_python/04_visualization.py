import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# Load Datasets
# ==========================

orders = pd.read_csv("../01_data/01_Raw/olist_orders_dataset.csv")
order_items = pd.read_csv("../01_data/01_Raw/olist_order_items_dataset.csv")
products = pd.read_csv("../01_data/01_Raw/olist_products_dataset.csv")
translation = pd.read_csv("../01_data/01_Raw/product_category_name_translation.csv")
customers = pd.read_csv("../01_data/01_Raw/olist_customers_dataset.csv")
reviews = pd.read_csv("../01_data/01_Raw/olist_order_reviews_dataset.csv")

# ==========================
# Revenue by Category
# ==========================

merged = order_items.merge(products, on="product_id", how="left")
merged = merged.merge(translation, on="product_category_name", how="left")

category_revenue = (
    merged.groupby("product_category_name_english")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))
category_revenue.plot(kind="bar")
plt.title("Top 10 Revenue Generating Categories")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../04_outputs/revenue_by_category.png")
plt.close()

# ==========================
# Monthly Sales Trend
# ==========================

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"],
    dayfirst=True,
    format="mixed"
)

orders["Month"] = orders["order_purchase_timestamp"].dt.to_period("M")

monthly = orders.merge(order_items,on="order_id")

monthly_sales = (
    monthly.groupby("Month")["price"]
    .sum()
)

plt.figure(figsize=(12,6))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("../04_outputs/monthly_sales_trend.png")
plt.close()

# ==========================
# State Wise Revenue
# ==========================

state = orders.merge(customers,on="customer_id")
state = state.merge(order_items,on="order_id")

state_sales = (
    state.groupby("customer_state")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))
state_sales.plot(kind="bar")
plt.title("Top 10 States by Revenue")
plt.xlabel("State")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("../04_outputs/state_revenue.png")
plt.close()

# ==========================
# Order Value Distribution
# ==========================

order_value = (
    order_items.groupby("order_id")["price"]
    .sum()
)

plt.figure(figsize=(8,6))
plt.hist(order_value,bins=30)
plt.title("Order Value Distribution")
plt.xlabel("Order Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("../04_outputs/order_value_distribution.png")
plt.close()

# ==========================
# Review Score Distribution
# ==========================

review_score = (
    reviews["review_score"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(7,7))
plt.pie(
    review_score,
    labels=review_score.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Customer Review Score Distribution")
plt.tight_layout()
plt.savefig("../04_outputs/review_distribution.png")
plt.close()

print("="*50)
print("All Visualizations Created Successfully!")
print("Saved inside : 04_outputs")
print("="*50)