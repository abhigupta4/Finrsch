import nltk
import requests
import re
from bs4 import BeautifulSoup
import urllib

site = ["http://ir.americanexpress.com/","http://investors.amgen.com/phoenix.zhtml?c=61656&p=irol-IRHome","http://www.caterpillar.com/en/investors.html","http://investors.anadarko.com/","http://investor.delphi.com/investors/investor-relations/default.aspx","http://www.gm.com/investors/index.html","http://ir.homedepot.com/","http://investor.lamresearch.com/","http://investor.mastercard.com/investor-relations/default.aspx","http://ir.prologis.com/"]

# r = requests.get("http://www.caterpillar.com/en/investors/events-and-presentations.html")
r = requests.get(site[5])
soup = BeautifulSoup(r.content,"lxml")
[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
visible_text = soup.getText()


print(visible_text)
# links = soup.find_all('a')
# for ele in links:
# 	print(ele)
print(soup)
# texts = document.findAll(text=True)
# print texts	
# print document