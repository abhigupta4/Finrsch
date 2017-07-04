import requests
from bs4 import BeautifulSoup
import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from newdb import add_to_db

def get_file(cur):
	base = 'https://www.sec.gov'
	r = requests.get(cur)
	document = BeautifulSoup(r.content,"lxml")
	links = document.find_all('a')
	for link in links:
		if 'Archives' in link.get("href"):
			return (base+link.get("href"))
			break


def take_second_link(cur,cik):
	begin = 'https://www.sec.gov'
	r = requests.get(cur)
	document = BeautifulSoup(r.content,"lxml")
	links = document.find_all('a')
	for link in links:
		temp = link.get("href")
		if 'edgar' in temp and 'index' in temp and 'headers' not in temp:
			fir = (begin + str(temp))
			break

	sec = ''
	for link in links:
		temp = link.get("href")
		if '.xlsx' in temp:
			sec = temp
			break

	return [fir, sec]	

def find_details(entire):
	begin = 'https://www.sec.gov/Archives/edgar/data/'
	for part in entire:
		if 'edgar' in part:
			temp = part.split('/')
			last = ''
			for ele in temp[-1]:
				if ele.isdigit():
					last += ele
	new = begin + temp[-2] + '/' + last
	for i in range(len(entire)):
		if 'edgar' in entire[i]:
			break

	for j in range(i-1,0,-1):
		if  entire[j] != '':
			break

	return [new,temp[-2],entire[j]]

def inside_index(link1):
	r = requests.get(main_link+link1)
	document = BeautifulSoup(r.content,"lxml")
	soup = document.get_text()
	lines = soup.split("\n")
	flag = 1
	for line in lines:
		temp = line.split(" ")
		for i in range(len(temp)):
			if temp[i] == '10-Q' or temp[i] == '10-K' and temp[i-1] == '' and temp[i+1] == '':
				quarter = '2' #Take quarter from here
				
				new, name, filing = find_details(temp) 
				#Take name and filing data from here
				
				new_li, financial = take_second_link(new, temp[-2])
				# Take excel link from here
				
				docu = get_file(new_li) 
				#This will be url variable
				html = request.urlopen(docu).read().decode('utf8')  
				# This is unstripped text
				
				raw = BeautifulSoup(html,"lxml").get_text()  
				# This is actual text
				
				tokens = tokenizer.tokenize(raw)   
				#This is the tokens variable
				
				add_to_db(name,docu,quarter,html,raw,str(tokens),filing,financial)
				break
		
tokenizer = RegexpTokenizer(r'\w+')
main_link = 'https://www.sec.gov/Archives/edgar/daily-index/2017/QTR2/'

r = requests.get(main_link)
document = BeautifulSoup(r.content,"lxml")
links = document.find_all('a')

for link in links:
	if 'company' in link.get("href") and '.idx' in link.get("href"):
		inside_index(link.get("href"))
		
