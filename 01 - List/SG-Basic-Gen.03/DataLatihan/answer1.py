data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(dataX):
	x = []
	with open(dataX) as data :
	    for line in data :
		    x = line.split()
	return x

temp = readData(data1)
txt = []
for i in temp:
        if (i == 'and') or (i == 'the') or (i == 'you') : txt.append('***')
        elif (i == 'And') or (i == 'The') or (i == 'You') : txt.append('***')
        elif (i == 'i') or (i == 'I'): txt.append('*')
        else : txt.append(i)

txt = ' '.join(txt)
print(txt)
