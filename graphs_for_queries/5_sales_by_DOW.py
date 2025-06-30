import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
units = [4, 8, 3, 10, 5, 7, 12]

color = '#1a73e8' 

plt.figure(figsize=(8, 5))
bars = plt.bar(days, units, color=color)


plt.grid(axis='y', color='lightgray', linestyle='--', linewidth=0.5)
plt.gca().set_axisbelow(True)
colors = ['#b3d1ff', '#99c2ff','#e6f0ff' , '#66a3ff', '#cce0ff', '#80b3ff', '#1a73e8']
bars = plt.bar(days, units, color=colors)
plt.xlabel('Day of Week')
plt.ylabel('Total Sold Units')
plt.title('Total Sold Units by Day of Week')
plt.tight_layout()
plt.show()