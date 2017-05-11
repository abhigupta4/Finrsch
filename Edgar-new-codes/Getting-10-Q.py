import requests
from bs4 import BeautifulSoup
import urlparse

def get_10_Q(cur):
	base = 'https://www.sec.gov'
	r = requests.get(cur)
	document = BeautifulSoup(r.content,"lxml")
	links = document.find_all('a')
	for link in links:
		if '10q' in link.get("href") or '10q' in link.get("href"):
			print 'Document link'
			print base+link.get("href")
			break

def take_second_link(cur,cik):
	begin = 'https://www.sec.gov'
	r = requests.get(cur)
	document = BeautifulSoup(r.content,"lxml")
	links = document.find_all('a')
	for link in links:
		temp = link.get("href")
		if 'index' in temp and 'headers' not in temp and cik in temp:
			print 'Company link'
			print begin+temp
			get_10_Q(begin + temp)

			# break

def find_link1(entire):
	begin = 'https://www.sec.gov/Archives/edgar/data/'
	for part in entire:
		if 'data' in part:
			temp = part.split('/')
			last = ''
			for ele in temp[-1]:
				if ele.isdigit():
					last += ele
	new = begin + temp[-2] + '/' + last
	take_second_link(new,temp[-2])

def inside_index(link1):
	r = requests.get(main_link+link1)
	document = BeautifulSoup(r.content,"lxml")
	soup = document.get_text()
	lines = soup.split("\n")
	flag = 1
	for line in lines:
		temp = line.split(" ")
		for i in xrange(len(temp)):
			if temp[i] == '10-Q' and temp[i-1] == '' and temp[i+1] == '':
				find_link1(temp)
				break

main_link = 'https://www.sec.gov/Archives/edgar/daily-index/2017/QTR2/'

r = requests.get(main_link)
document = BeautifulSoup(r.content,"lxml")
links = document.find_all('a')

for link in links:
	if 'company' in link.get("href") and '.idx' in link.get("href"):
		inside_index(link.get("href"))