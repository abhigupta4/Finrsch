import nltk
from bs4 import BeautifulSoup

def remove_non_ascii_1(text):

    return ''.join(i for i in text if ord(i)<128)



file1 = open("0000826083-11-000006.txt","r")

data = file1.read()

cleaned = remove_non_ascii_1(data)

soup = BeautifulSoup(cleaned,"lxml")
# print(soup)
visible_text = soup.getText()
print(visible_text)
