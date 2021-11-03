import numpy as np
A = np.array([[5, -2],[7,-4]],dtype=float)
eigValue,eigVector = np.linalg.eig(A);
print(eigValue)
print(eigVector)
