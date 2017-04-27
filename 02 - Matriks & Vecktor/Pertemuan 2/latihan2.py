import numpy as np
M = np.mat("1 -2;1 4")
eigenvalue, eigenvector = np.linalg.eig(M)
print("eigen value : ")
print(eigenvalue)
print("eigenvector : ")
print(eigenvector)
