from sympy import solve
from sympy import symbols
x, y, z = symbols('x y z')

# Tehtävä 1

A = solve([x - 2*y - 2*z, -2*x + y - z + 3, 3*x + 2*y + z - 4], [x, y, z], dict=True)
print(f"Yhtälöryhmän ratkaisu on: ", A)

B = solve([x + y - 1, 2*x + y - z - 1, 3*x + y - 2*z - 1], [x, y, z], dict=True)
print(f"Yhtälö on aina tosi, kun: ", B)

# Tehtävä 2

C = solve([2*x + 4*y - z - 11, 6*x - y - 3*z - 7, 4*x + 5*y - 2*z - 16], [x, y, z], dict=True)
print(f"Yhtälö in aina tosi, kun: ", C)

D = solve([4*x + 2*y - 2*z, 2*x + y - z - 1, 3*x + y - 2*z - 1], [x, y, z], dict=True)
print(f"Yhtälö on epätosi kaikilla x, y, z: ", D)

# Kertaustehtävät

E = solve([5*x + 3*y - 9, 2*x + y - 4], [x, y], dict=True)
print("Yhtälöparin ratkaisu on: ", E)

F = solve([2*x + y + z - 6, x + 3*y + z - 2, 2*x + y + 2*z - 9], [x, y, z], dict=True)
print(f"Yhtälöryhmän ratkaisu on: ", F)

G = solve([x + y + 3*z + 1, 3*x + y + z - 5, 2*x + y + 2*z - 2], [x, y, z], dict=True)
print(f"Yhtälöryhmän ratkaisu on: ", G)

