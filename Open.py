#! /usr/bin/env python
__author__ = 'Alex'


import webbrowser

def chrome(url):
	webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
print("Enter a url or enter a number of your top sites")
print(" 0) Google")
print(" 1) MAIN CS61B")
print(" 2) PROJECT0  ::  due 1/29")
print(" 3) ")

print()
url = input("Enter a url" + "\n")

if url == "0":
	chrome("http://google.com")
elif url == "1":
	chrome("http://cs61b.ug/sp16/")
elif url == "2":
	chrome("http://cs61b.ug/sp16/materials/proj/proj0/proj0.html")
else:
	chrome(url)