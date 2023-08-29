import numpy as np

# 1. Määrittele ja esitä 5-alkioinen kokonaislukutaulukko numpyn avulla. luvut voivat olla satunnaisia.
array = np.random.randint(1, 10, size=5)
print(array)

# 2. Sinulla on vektorit a) u = 2i + 3j, v =4i - 7j
# b) uu= i + j + k, vv 3i -3j + 2k.
# Määrittele nämä numpy taulukon avulla

u = np.array([2, 3])  # Vektori u = 2i + 3j
v = np.array([4, -7])  # Vektori v = 4i - 7j

uu = np.array([1, 1, 1])  # Vektori uu = i + j + k
vv = np.array([3, -3, 2])  # Vektori vv = 3i - 3j + 2k

print("Vektori u:", u)
print("Vektori v:", v)
print("Vektori uu:", uu)
print("Vektori vv:", vv)

# 3. Laske kunkin vektorin normi.

norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)
norm_uu = np.linalg.norm(uu)
norm_vv = np.linalg.norm(vv)

print(f"Vektori u:n normi: {norm_u:.2f}")
print(f"Vektori v:n normi: {norm_v:.2f}")
print(f"Vektori uu:n normi: {norm_uu:.2f}")
print(f"Vektori vv:n normi: {norm_vv:.2f}")