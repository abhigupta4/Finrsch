import os

def give_quart(fiscal, filed):
	fiscal = int(fiscal)
	filed = int(filed)
	fiscal -= 1
	filed -= 1
	for i in xrange(4):
		for j in xrange(1,4):
			if filed == (fiscal+ 3*i + j)%12 :
				return str(i+1)

def build(main_path, all_files):
	ind1 = open(main_path + '/index.txt','w')
	for fil in all_files:
		ind1.write('Name of file ' + fil+'\n')
		cur = open(main_path + '/' + fil,'r')
		data = cur.readlines()
		flag = 1
		for line in data:
			if 'COMPANY CONFORMED NAME' in line:
				spaces = ' '.join(line.split(':')[-1].split())
				ind1.write('Company name is ' + spaces + '\n')
		for line in data:
			if 'CONFORMED' in line and 'SUBMISSION' in line:
				ind1.write('Type is ' + line.split()[-1] + '\n')
				if 'Q' in line:
					flag = 0
				break 

		for line in data:
			if 'FILED' in line and 'DATE' in line:
				ind1.write('Filed date is ' + line.split()[-1] + '\n')

		if not flag:
			for line in data:
				if 'FISCAL' in line:
					fis = line.split()[-1]
					break

			for line in data:
				if 'CONFORMED' in line and 'PERIOD' in line:
					date = line.split()[-1]
					break

			ind1.write('Quarter number ' + give_quart((fis[-4]+fis[-3]), (date[-4]+date[-3])) + '\n')
		cur.close()
		ind1.write('\n')

	ind1.close()

for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
	fold = dirnames
	break	

kaam = []
for f in fold:
	for (a,b,file1) in os.walk(os.getcwd() + '/' + f):
		build(os.getcwd() + '/' + f, file1)
		break

