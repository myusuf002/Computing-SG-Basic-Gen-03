data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(dataX):
  x = []
  with open(dataX) as data :
    for line in data :
      x = line.split()
  return x

txt = readData(data1) + readData(data2)
temp = []
for i in txt:
  if i not in temp:
    temp.append(i)

for i in temp:
  print(i)
