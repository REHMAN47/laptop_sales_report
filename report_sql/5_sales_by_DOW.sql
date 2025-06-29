--total laptop sales by day of the week
SELECT 
    COUNT(product_id) AS total_sold_units,
    TO_CHAR(sale_date, 'Day') AS day_of_week
FROM  
    laptop_sales
GROUP BY 
    TO_CHAR(sale_date, 'Day');