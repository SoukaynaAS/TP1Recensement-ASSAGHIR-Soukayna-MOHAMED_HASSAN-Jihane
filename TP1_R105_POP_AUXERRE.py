import csv
A_pop=[]
d_2008=[]
with open('donnees_2008.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        d_2008.append(row)

#print(d_2008)

n_2008=0
for i in range(len(d_2008)):
	if d_2008[i][6]=='Auxerre':
		A_pop.append(d_2008[i][9])
#		print(d_2008[i][9])
		n_2008=i
#print(n_2008)

d_2016=[]
with open('donnees_2016.csv',newline='') as csvfile:
	reader=csv.reader(csvfile,delimiter=',')
	for row in reader:
		d_2016.append(row)
#print(d_2016)
n_2016=0
for i in range(len(d_2016)):
	if d_2016[i][6]=='Auxerre':
		A_pop.append(d_2016[i][9])
#		print(d_2016[i][9])
		n_2016=i
#print(n_2016)

d_2021=[]
with open('donnees_2021.csv',newline='') as csvfile:
	reader=csv.reader(csvfile,delimiter=';')
	for row in reader:
		d_2021.append(row)
#print(d_2021)
n_2021=0
for i in range(len(d_2021)):
	if d_2021[i][2]=='89024':
		A_pop.append(d_2021[i][5])
#		print(d_2021[i][5])
		n_2021=i
#print(n_2021)

d_2023=[]
with open('donnees_2023.csv',newline='') as csvfile:
	reader=csv.reader(csvfile,delimiter=';')
	for row in reader:
		d_2023.append(row)
#print(d_2023)
n_2023=0
for i in range(len(d_2023)):
	if d_2023[i][7]=='Auxerre':
		A_pop.append(d_2023[i][10])
#		print(d_2023[i][10])
		n_2023=i
#print(n_2023)

from matplotlib import pyplot as plt
dates=[2023,2021,2016,2008]

plt.plot(dates,A_pop,color='b')
plt.scatter(dates,A_pop,color='r')
plt.title("Population à Auxerre entre 2008 et 2023")
plt.ylabel('Population')
plt.xlabel('Années')

plt.show()




