M = [[12,7], [4,5], [3,8]]
#Transpose Matriks
T = [[x[i] for x in M] for i in range(len(M[0]))]
for i in T:
  print(i)

#Transpose Matriks with Numpy
import numpy as np
print(np.transpose(M))
