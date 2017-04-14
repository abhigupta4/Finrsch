fi = open("500companies.txt","r")

sp = []
for line in fi.readlines():
	sp.append(line.split()[0])

print sp