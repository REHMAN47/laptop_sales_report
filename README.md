# Introduction
📋This project explores and analyzes a dataset of 💻 laptop sales using SQL. The goal is to derive valuable 📊 business insights, detect 📈 sales trends, and uncover patterns across 🕒 time, 🏷️ brands, 📐 screen sizes, 💽 operating systems, and 📆 days of the week.

🔍 SQL Queries ? Check them out here : [report_sql_folder](/report_sql/)
# Background
In today’s data-driven world, businesses rely heavily on data analytics to make informed decisions. The consumer electronics market, particularly the 💻 laptop segment, is highly competitive and fast-evolving. Companies need to track and understand their sales performance, customer preferences, and product trends to stay ahead.

Using advanced SQL techniques such as:

- CASE for conditional logic,

- WITH (CTEs) for modular query building,

- RANK() for identifying top performers, and

- TO_CHAR() / EXTRACT() for date manipulation,

### Questions I Wanted to answer through my SQL queries were :
1. What is the sales distribution between Windows 10 and Windows 11 laptops in the past month?
2. Which laptop model achieved the highest sales volume last month?
3. Which CPU brands or models led in laptop sales?
4. What is the distribution of laptop sales across different dates?

# Tools I Used
📊 **Excel** **:** 
Handled initial data import, formatting, and preprocessing before loading into PostgreSQL.

🐘**PostgreSQL** **:**
Used for querying, transforming, and analyzing the laptop sales dataset using advanced SQL functions.

🧑‍💻 **GitHub** **:**
Used for version control, organizing SQL scripts, and documenting the entire analysis workflow.

🐍 **Python** **:** Used to generate clean and insightful visualizations using the Matplotlib library.
It transformed SQL query outputs into readable charts like bar graphs and trend lines.
Custom styles, colors, labels, and gridlines were added to highlight key insights effectively.




# The Analysis
Each query of this project aimed to derive valuable business insights, detect sales trends, and uncover patterns across time, brands, screen sizes, operating systems, and days of the week.

### 1. Sales distribution between Windows 10 and Windows 11
I selected the os column to group the data based on each unique operating system (like Windows 10 or 11).
Then I used COUNT(*) to count how many laptops fall under each OS. This gives us the total units sold per operating system.
I added GROUP BY os to ensure the counting is done per OS category, not across the whole table.
Finally, ORDER BY total_laptops DESC sorts the results so the most popular OS appears at the top.

```sql
SELECT 
    os,COUNT(*) AS total_laptops
FROM 
    laptop_sales
GROUP BY os;
```

The data shows a clear preference for Windows 11 OS, which accounts for the majority of laptop sales with 45 units sold, compared to just 4 units for Windows 10 OS. This suggests that most customers are opting for newer systems, possibly due to better performance, features, or future support. The shift highlights a strong market trend toward adopting the latest Windows version in newly sold laptops.



# What I Learned

# Conclusion