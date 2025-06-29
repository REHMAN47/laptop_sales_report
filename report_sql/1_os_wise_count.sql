--Total number of latops on the basis of OS
SELECT 
    os,COUNT(*) AS total_laptops
FROM 
    laptop_sales
GROUP BY os;