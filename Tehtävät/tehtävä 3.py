<<<<<<< HEAD
from sympy import solve
from sympy import symbols
x, y, z = symbols('x y z')

# Tehtävä 1

A = solve([x - 2*y - 2*z, -2*x + y - z + 3, 3*x + 2*y + z - 4], [x, y, z], dict=True)
print(A)

B = solve([x + y - 1, 2*x + y - z - 1, 3*x + y - 2*z - 1], [x, y, z], dict=True)
print(B)

# Tehtävä 2

C = solve([2*x + 4*y - z - 11, 6*x - y -3*z - 7, 4*x + 5*y - 2*z - 16], [x, y, z], dict=True)
print(C)

D = solve([4*x + 2*y - 2*z, 2*x + y - z - 1, 3*x + y - 2*z - 1], [x, y, z], dict=True)
print(D)

# Kertaustehtävät

E = solve([5*x + 3*y - 9, 2*x + y - 4], [x, y], dict=True)
print(E)

F = solve([2*x + y + z - 6, x + 3*y + z - 2, 2*x + y + 2*z - 9], [x, y, z], dict=True)
print(F)

G = solve([x + y + 3*z + 1, 3*x + y + z - 5, 2*x + y + 2*z - 2], [x, y, z], dict=True)
print(G)
=======
import numpy as np

# Tehtävä 1

A = np.array([[-1, 2], [3, -5]])
B = np.array([[2, 0], [-1, 4]])
print("Matriisi A= ", A)
print("Matriisi B= ", B)
print("2A+3B= ", 2*A+3*B)
print("A-B= ", A-B)


# Tehtävä 2
# Aiemmin määriteltiin matriisi A, joten:


A2 = np.array([[2, 3, 1], [0, 7, -2]])

for i in range(1,3):
    for j in range(1,4):
        A2[i-1][j-1]=A2[i-1][j-1]*(i+1)

print("(1+i)A= ", A2)
>>>>>>> origin/master
