--Best seller of last month
SELECT 
       product_name,
       screen_size,
       SUM(price) AS best_seller,
       COUNT(product_name) AS total_units_sold
FROM 
       laptop_sales
GROUP BY 
       product_name,
       screen_size
ORDER BY 
       total_units_sold DESC
LIMIT 10;