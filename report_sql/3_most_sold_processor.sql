--Most selling processor
SELECT CASE 
       		WHEN processor LIKE '%Intel%' THEN 'Intel'
    		WHEN processor LIKE '%Ryzen%' THEN 'Ryzen'
    		ELSE 'Other'
 	   END AS processor_type,
       COUNT(*) AS total_laptops 
FROM 
    laptop_sales
GROUP BY 
    processor_type
ORDER BY total_laptops DESC;

--If you want confirm that the qurey is returning all rows or not
WITH units_sold_per_day AS(
	SELECT 
        COUNT(product_id) AS total_sold_units,
	    EXTRACT(ISODOW FROM sale_date) AS day_of_week
	FROM 
        laptop_sales
	GROUP BY 
        day_of_week
	ORDER BY day_of_week ASC
)
SELECT 
    SUM(total_sold_units)
FROM 
    units_sold_per_day;