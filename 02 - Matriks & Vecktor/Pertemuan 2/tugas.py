A = [[1, 2, 3]]
B = [[1,2,3], [4,5,6], [7,8,9]]

"""
for i in A:
	print(i[0])

for j in B:
	for k in j:
		print(k)
"""
x = 0
y = 0
X = A
Y = B
Z = []
while x < len(X):
	y = 0
	count = 0
	while y < len(X[x]):
		count = count + X[x][x] * Y[y][y]
		Z.append(count)
		y+=1
	x+=1

print(y)
print(Z)	
