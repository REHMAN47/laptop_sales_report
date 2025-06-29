--Number of laptops sold on each date of the month
SELECT 
    sale_date, 
    COUNT(*) AS total_laptops_sold
FROM 
    laptop_sales
GROUP BY 
    sale_date
ORDER BY sale_date ASC;