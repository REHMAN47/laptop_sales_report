import matplotlib.pyplot as plt
import pandas as pd

data = {
    "sale_date": [
        "2025-05-01", "2025-05-02", "2025-05-04", "2025-05-06", "2025-05-08",
        "2025-05-09", "2025-05-10", "2025-05-11", "2025-05-12", "2025-05-13",
        "2025-05-15", "2025-05-16", "2025-05-17", "2025-05-18", "2025-05-19",
        "2025-05-20", "2025-05-21", "2025-05-22", "2025-05-23", "2025-05-24",
        "2025-05-25", "2025-05-26", "2025-05-27", "2025-05-30"
    ],
    "total_laptops_sold": [2, 1, 2, 1, 4, 1, 1, 2, 2, 5, 2, 1, 3, 6, 1, 1, 3, 2, 1, 3, 2, 1, 1, 1]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))
bars = plt.bar(df["sale_date"], df["total_laptops_sold"], color='#1a73e8')
plt.grid(axis='y', color='lightgray', linestyle='--', linewidth=0.5)
plt.gca().set_axisbelow(True)
plt.xlabel('Sale Date')
plt.ylabel('Total Laptops Sold')
plt.title('Total Laptops Sold by Date')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
