import csv
file_bands=[]
with open('file_bands.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        file_bands.append(row)
#print(file_bands)
del file_bands[0]
#print(file_bands)
#add=['Chika','Choko','1990','2','50']
#file_bands.append(add)
#print(file_bands)
somme=0
for i in range (len(file_bands)):
	file_bands[i][4]=int(file_bands[i][4])
	somme+=int(file_bands[i][4])
moyenne=somme/len(file_bands)
print(somme)
print(moyenne)

