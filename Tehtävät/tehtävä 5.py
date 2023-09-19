import numpy as np

# TEHTÄVÄ 1

# 1a
m1 = np.array([[-1, 2], [3, 1]])
m2 = np.array([[0, 1, 3], [2, -3, 5]])
m3 = np.dot(m1, m2)
print("Tehtävän 1a vastaus: ")
print(m3)

# 1b
m1 = np.array([[1, 3, 5], [0, -2, 1], [2, -1, 4]])
m2 = np.array([[1], [-3], [-1]])
m3 = np.dot(m1, m2)
print("Tehtävän 1b vastaus: ")
print(m3)

# 1c
m1 = np.array([[2, 0, 1], [1, -3, 4], [0, 1, 5]])
m2 = np.array([[3], [-5], [7]])
m3 = np.dot(m1, m2)
print("Tehtävän 1c vastaus: ")
print(m3)

# 1d
m1 = np.array([[1, -4, 2], [3, 0, -2], [2, 1, 0]])
m2 = np.array([[5, 1, -1], [-2, 1, 3], [0, 3, 4]])
m3 = np.dot(m1, m2)
print("Tehtävän 1d vastaus: ")
print(m3)


# TEHTÄVÄ 2

# Tehtävä 1

# A
a = np.array([[4, 9, 0], [-3, 7, -11]])
print("Ensimmäisen matriisin transpoosi: ")
print(np.transpose(a))

# B
a = np.array([[8, 9], [-3, 12], [0, -1], [7, 1]])
print("Toisen matriisin transpoosi: ")
print(np.transpose(a))

# Tehtävä 2

# 1a
a = np.array([[5, -6], [8, 10]])
print("Tehtävä 1a: Determinantti on ")
print(f"{np.linalg.det(a):.0f}")

# 1b
x=1
a = np.array([[1-x, -x], [x, 1-x]])
print("Tehtävä 1b: Determinantti on ")
print(f"{np.linalg.det(a):.0f}")

# 2a
a = np.array([[2, 3, 4], [-2, -1, 1], [5, 3, 2]])
print("Tehtävä 2a: Determinantti on ")
print(f"{np.linalg.det(a):.0f}")

# 2b
a = np.array([[3, 15, 7], [0, -4, 0], [3, 2, 3]])
print("Tehtävä 2b: Determinantti on ")
print(f"{np.linalg.det(a):.0f}")

# Tehtävä 3

a = np.array([[-2, 0, 8, 5], [3, -1, 2, 1], [4, 7, 6, 2], [1, 0, 2, 3]])
print("Tehtävä 3: Determinantti on")
print(f"{np.linalg.det(a):.0f}")
