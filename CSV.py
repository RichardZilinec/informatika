import csv
#
subor = open('data.csv', 'r', encoding='utf-8')
reader = csv.reader(subor)
header = next(reader)
vyskyt = []
#
#
#
for i in range(1,10):
    vyskyt[i] = 0

for row in reader:
    vsetky_hodnoty = [row[5] for row in reader]

for i in range(len(vsetky_hodnoty)):
    prve_cislo = str(vsetky_hodnoty[i])[0]