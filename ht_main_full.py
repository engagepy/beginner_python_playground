import requests 
from bs4 import BeautifulSoup 
from time import sleep as sl

def news(): 
	# the target we want to open	 
	url='http://www.hindustantimes.com'
	
	#open with GET method 
	resp=requests.get(url) 
	
	#http_respone 200 means OK status 
	if resp.status_code==200: 
		print("Successfully opened the web page. \n") 
		sl(1)
		print("The news are as follow :-\n")
	
		# we need a parser,Python built-in HTML parser is enough . 
		soup=BeautifulSoup(resp.text,'html.parser')	 

		# l is the list which contains all the text i.e news 
		l=soup.find("div",{"class":"new-topnews-left"})
		#this was ad hoc experiment, as some news was getting left out
		z=soup.find("div",{"class":"container border-bottom pb-20 mt-30"})
	
		#now we want to print only the text part of the anchor. 
		#find all the elements of a, i.e anchor 
		for i in l.findAll("a"): 
			print(i.text)
		#repeated the function for z part of the page
		for i in z.findAll("a"): 
			print(i.text) 	
	else: 
		print("Error") 
		
news()
input()

