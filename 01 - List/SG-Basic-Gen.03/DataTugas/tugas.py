data1 = "DataSet.txt"

def readData(dataX):
	x = []
	with open(dataX) as data :
	    for line in data :
		    x = line.split()
	return x

txt = readData(data1)
i = 0
ebi = []

while i < len(txt)-1:
	if i == 0:
		ebi.append(txt[i].capitalize())
		i +=1
	elif txt[i][len(txt[i])-1] == '.':
		temp = txt[i+1].replace(txt[i+1][0], txt[i+1][0].upper(), 1)
		ebi.append(txt[i])
		ebi.append(temp)
		i +=2
	else:
		ebi.append(txt[i])
		i +=1

num = []
for j in ebi:
	if j.isnumeric():
		num.append(j)

print(num)
list.reverse(num)

n = 0
j = 0
fix = []
while j < len(ebi):
	if ebi[j].isnumeric():
		fix.append(num[n])
		n +=1
	else:
		fix.append(ebi[j])
	j +=1
	

fix = ' '.join(fix)
print(fix)
