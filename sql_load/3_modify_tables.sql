COPY laptop_sales
FROM 'C:\Users\Shaik Rehman\Desktop\SQL_Project_Data_Job_Analyst\csv_files\laptop_sales.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8');
