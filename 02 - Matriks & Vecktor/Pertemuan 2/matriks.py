import numpy as np

a = np.array([[1,2,3],
              [2,5,6],
              [3,8,9]])
b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
c = np.array([[1,2,3]])

d = np.array([[1,4,7]])

print(a+b,'\n')  				#penjumlahan matriks
print(np.dot(c,b),'\n')			#perkalian matriks
print(np.transpose(c),'\n')		#ranspose matriks
print(np.transpose(d),'\n')


