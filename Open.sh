#! /usr/bin/env python
__author__ = 'Alex'


import webbrowser
sites = [" 0) Google",
		 " 1) MAIN CS61B",
		 " 2) Github",
		 " 3) CalCentral"]
homework = [" q) PROJECT0  ::  due 1/29",
			" w) MATH HW  ::  due 1/29"]

def chrome(url):
	webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
print("Enter a url or enter a number of your top sites")
print()
for x in sites:
	print(x)
print()	
print("- " * 20)
print()
for x in homework:
	print(x)
print("=" * 40)
print()
url = input("Enter a url" + "\n")

if url == "0":
	chrome("http://google.com")
elif url == "1":
	chrome("http://cs61b.ug/sp16/")
elif url == "2":
	chrome("https://github.com")
elif url == "3":
	chrome("https://calcentral.berkeley.edu")
elif url == "q":
	chrome("http://cs61b.ug/sp16/materials/proj/proj0/proj0.html")
elif url == "w":
	chrome("https://math.berkeley.edu/~apaulin/1Bhome1.pdf")	
else:
	chrome(url)