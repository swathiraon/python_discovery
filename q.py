import requests
from bs4 import BeautifulSoup

url='http://blog.speckbit.com/10-things-they-wont-tell-you-in-college/'
r=requests.get(url)

soup=BeautifulSoup(r.text,'html.parser')

p=soup.find_all('li')
l=soup.find_all('p')
i=0

while i<len(p):
	print(p[i].get_text())
	i+=1

	

i=0

while i<len(l):
	print(l[i].get_text())
	i+=1
