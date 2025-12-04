import csv
departement_2008=[]
with open('donnees_2008.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        departement_2008.append(row)
print(departement_2008)

n=0
for i in range(len(departement_2016)):
	if departement_2016[i][3]=='89':
		print(departement_2016[i][7])
n+=i
print("la somme est=",n)

departement_2016=[]
with open('donnees_2016.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        departement_2016.append(row)
print(departement_2016)

n=0
for i in range(len(departement_2016)):
	if departement_2016[i][2]=='89':
		print(departement_2016[i][9])
n+=i
print("la somme est=",n)

departement_2021=[]
with open('donnees_2021.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        departement_2021.append(row)
print(departement_2021)

n=0
for i in range(len(departement_2021)):
	if departement_2021[i][1]=='89':
		print(departement_2021[i][5])
n+=i
print("la somme est=",n)

departement_2023=[]
with open('donnees_2016.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        departement_2023.append(row)
print(departement_2023)

n=0
for i in range(len(departement_2023)):
	if departement_2023[i][2]=='89':
		print(departement_2023[i][10])
n+=i
print("la somme est=",n)
