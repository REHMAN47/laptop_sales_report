import matplotlib.pyplot as plt

# Data
labels = ["Intel (32)", "Ryzen (16)", "Other (1)"]
sizes = [32, 16, 1]

colors = ['#1a73e8', '#99c2ff', '#e6f0ff']

plt.figure(figsize=(5, 5))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Laptop Distribution by Processor Type',pad=30)
plt.legend(title = 'Total : 49',bbox_to_anchor=(1, 1))
plt.axis('equal')
plt.show()