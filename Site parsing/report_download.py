import requests
from bs4 import BeautifulSoup
import urlparse

visi = {}

testing_sites = ['http://www.energyrecovery.com', 'http://www.agilent.com/home', 'http://www.altria.com/Pages/default.asp', 'http://www.conocophillips.com/Pages/default.asp', 'http://www.conagrabrands.com', 'https://www.cmegroup.com', 'http://www.garmin.com/en-US', 'http://www.generaldynamics.com', 'http://www.gm.com/index.htm', 'https://www.mastercard.com', 'http://www.ge.com', 'http://www.caterpillar.com']

def pdf_down(link1):
	if 'code' in link1 or 'Code' in link1:
		return
	r = requests.get(link1)
	print 'Downloading ' +  link1.split('/')[-1]
	with open('Downloaded/' + link1.split('/')[-1] + '.pdf', 'wb') as f:
		f.write(r.content)
		f.close()
	print 'Downloaded'


def exter_down(link1,name):
	try:
		r = requests.get(link1)
		print 'Downloading ' + name
		with open('Downloaded/' + name + '.pdf', 'wb') as f:
			f.write(r.content)
			f.close()
		print Downloaded
	except:
		return


investing = []
finan = []

main_link  = testing_sites[9]
print 'At ' + main_link
r = requests.get(main_link)
document = BeautifulSoup(r.content,"lxml")
links = document.find_all('a')
# print links
for link in links:
	try:
		name = link.get_text().lower()
		cur_link = link.get('href')
		cur_link = urlparse.urljoin(main_link, cur_link)
		# print cur_link
		if 'invest' in name:
			if cur_link not in visi:
				investing.append(cur_link)
				visi[cur_link] = 1
		elif 'finan' in name or 'annual' in name or 'report' in name or 'proxy' in name:
			if cur_link not in visi:
				if '.pdf' in cur_link:
					pdf_down(cur_link)
				elif 'External' in cur_link:
					exter_down(cur_link, actual)
				else:
					finan.append(cur_link)
				visi[cur_link] = 1
	except:
		pass

while len(investing):
	cur = investing.pop()
	print 'At ' + cur
	if '.pdf' in cur:
		pdf_down(cur)
		continue
	elif 'External' in cur:
		exter_down(cur, actual)
		continue
	r = requests.get(cur)
	document = BeautifulSoup(r.content,"lxml")
	links = document.find_all('a')
	for link in links:
		try:
			name = link.get_text().lower()
			cur_link = link.get('href')
			cur_link = urlparse.urljoin(cur, cur_link)
			# print cur_link
			if 'finan' in name or 'quarter' in name or 'annual' in name or 'report' in name or 'proxy' in name:
				if cur_link not in visi:
					# print 'hi ' + name
					# print cur_link
					visi[cur_link] = 1
					if '.pdf' in cur_link:
						pdf_down(cur_link)
					elif 'External' in cur_link:
						exter_down(cur_link, actual)
					else:
						finan.append(cur_link)
		except:
			continue	

while len(finan):
	cur = finan.pop()
	print 'In ' + cur
	r = requests.get(cur)
	document = BeautifulSoup(r.content,"lxml")
	links = document.find_all('a')	
	for link in links:
		try:
			name = link.get_text().lower()
			actual = link.get_text()
			if name.split() == []:
				continue
			cur_link = link.get('href')
			cur_link = urlparse.urljoin(cur, cur_link)
			if cur_link not in visi:
				if '.pdf' in cur_link:
					pdf_down(cur_link)
					visi[cur_link] = 1
				elif 'External' in cur_link:
					exter_down(cur_link, actual)
					visi[cur_link] = 1
				elif 'quarter' in name or 'annual' in name or 'report' in name or 'proxy' in namex:
					finan.append(cur_link)
					visi[cur_link] = 1

		except:
			continue	
