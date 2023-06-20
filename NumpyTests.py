import numpy as np

K0 = np.array([[1,0]])
K1 = np.array([[0,1]])

# Test states Ψ, Φ
psi = np.sqrt(0.75)*K0 + np.sqrt(0.25)*K1
phi = np.sqrt(0.3)*K0 + np.sqrt(0.7)*K1

# Gate
H = np.matrix([[1/np.sqrt(2), -1/np.sqrt(2)], [1/np.sqrt(2), 1/np.sqrt(2)]])