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

