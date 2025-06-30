import matplotlib.pyplot as plt

products = [
    "Dell XPS 9720",
    "Asus UX581LV-H2035T",
    "MSI Stealth GS77 12UHS-226IN",
    "Asus ROG Zephyrus G14 2023",
    "Razer Blade 15 Advanced Gaming Laptop",
    "HP Victus 15-fa1066TX",
    "Asus ROG Flow X13 GV301QH-K5459TS",
    "Asus ROG Strix Scar 17 2023",
    "HP Victus 15-fb0106AX",
    "HP Victus 16-d0302TX"
]
units_sold = [2, 2, 1, 1, 1, 1, 1, 1, 1, 1]


colors = [

    "#1144a8","#155bcb","#1a73e8","#2c6ff2","#3d7ef5",
    "#5e9af7","#7ab4f8","#a1c9fb","#c8e3fc","#e8f0fe"
]

plt.figure(figsize=(10, 6))
plt.barh(products, units_sold, color=colors)
plt.xlabel('Total Units Sold')
plt.title('Total Units Sold by Product')
plt.tight_layout()
plt.show()