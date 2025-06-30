import matplotlib.pyplot as plt

os = ["Windows 10 OS", "Windows 11 OS"]
laptops = [4, 45]
colors = ['#7ab4f8', '#1a73e8']

plt.figure(figsize=(6, 6))
plt.bar(os, laptops, color=colors)
plt.grid(axis='y', color='lightgray', linestyle='--', linewidth=0.5)
plt.gca().set_axisbelow(True)
plt.xlabel('Operating System')
plt.ylabel('Total Laptops')
plt.title('Total Laptops by OS')
plt.show()