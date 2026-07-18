-- ============================================
-- E-Commerce Sales Analysis SQL Queries
-- ============================================

-- 1. Total Orders
SELECT COUNT(*) AS Total_Orders
FROM olist_orders_dataset;

------------------------------------------------

-- 2. Total Revenue
SELECT ROUND(SUM(price),2) AS Total_Revenue
FROM olist_order_items_dataset;

------------------------------------------------

-- 3. Average Order Value
SELECT ROUND(AVG(order_total),2) AS Average_Order_Value
FROM
(
    SELECT order_id,
           SUM(price) AS order_total
    FROM olist_order_items_dataset
    GROUP BY order_id
) t;

------------------------------------------------

-- 4. Top 10 Revenue Categories

SELECT
t.product_category_name_english,
ROUND(SUM(i.price),2) AS Revenue

FROM olist_order_items_dataset i

JOIN olist_products_dataset p
ON i.product_id=p.product_id

JOIN product_category_name_translation t
ON p.product_category_name=t.product_category_name

GROUP BY t.product_category_name_english

ORDER BY Revenue DESC

LIMIT 10;

------------------------------------------------

-- 5. Top 10 States by Revenue

SELECT

c.customer_state,

ROUND(SUM(i.price),2) AS Revenue

FROM olist_customers_dataset c

JOIN olist_orders_dataset o
ON c.customer_id=o.customer_id

JOIN olist_order_items_dataset i
ON o.order_id=i.order_id

GROUP BY c.customer_state

ORDER BY Revenue DESC

LIMIT 10;

------------------------------------------------

-- 6. Monthly Revenue

SELECT

TO_CHAR(order_purchase_timestamp,'YYYY-MM') AS Month,

ROUND(SUM(price),2) AS Revenue

FROM olist_orders_dataset o

JOIN olist_order_items_dataset i
ON o.order_id=i.order_id

GROUP BY Month

ORDER BY Month;

------------------------------------------------

-- 7. Review Score Distribution

SELECT

review_score,

COUNT(*) AS Total

FROM olist_order_reviews_dataset

GROUP BY review_score

ORDER BY review_score;

------------------------------------------------

-- 8. Top 10 Sellers

SELECT

seller_id,

ROUND(SUM(price),2) AS Revenue

FROM olist_order_items_dataset

GROUP BY seller_id

ORDER BY Revenue DESC

LIMIT 10;

------------------------------------------------

-- 9. Average Freight Cost

SELECT

ROUND(AVG(freight_value),2) AS Average_Freight

FROM olist_order_items_dataset;

------------------------------------------------

-- 10. Order Status Count

SELECT

order_status,

COUNT(*) AS Total

FROM olist_orders_dataset

GROUP BY order_status

ORDER BY Total DESC;