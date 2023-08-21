import math
from tabulate import tabulate

# tehtävä 1

# 1a
print(f"Muunna asteiksi: {int(math.degrees(2.493))}")
# 1b
print(f"Muunna asteiksi: {int(math.degrees(0.911))}")

# 2a
print(f"Muunna radiaaneiksi: {(math.radians(137.7)):.3f}")
# 2b
print(f"Muunna radiaaneiksi: {(math.radians(62.3)):.3f}")

# 3
table = [['Asteet', 'Radiaanit'],
         ['30', round(math.radians(30), 3)],
         ['45', round(math.radians(45), 3)],
         ['60', round(math.radians(60), 3)],
         ['90', round(math.radians(90), 3)],
         ['120', round(math.radians(120), 3)],
         ['135', round(math.radians(135), 3)],
         ['150', round(math.radians(150), 3)],
         ['180', round(math.radians(180), 3)],
         ['270', round(math.radians(270), 3)],
         ['360', round(math.radians(360), 3)]]

print(tabulate(table))

# tehtävä 2

print(f"Hypotenuusan pituus: {(math.hypot(2.3, 4.7)):.3f}")
print(f"Kolmion toinen kulma: {math.degrees((math.acos(2.3 / 5.233))):.2f} astetta.")
print(f"Kolmion kolmas kulma: {180 - 90 - 63.3:.2f} astetta.")

# tehtävä 3

print(f"Luvun 0 kertoma: {(math.factorial(0))}")
print(f"Luvun 4 kertoma: {(math.factorial(4))}")
print(f"Luvun 7 kertoma: {(math.factorial(7))}")
print(f"Luvun 15 kertoma: {(math.factorial(15))}")