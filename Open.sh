#! /usr/bin/env python
__author__ = 'Alex'


import webbrowser
bookmark = [" 0) Google",
		 " 1) MAIN CS61B",
		 " 2) Github",
		 " 3) CalCentral",
		 " 4) IRC help"
		]
homework = [" q) ",
			" w) "]
sites = {0 : "http://google.com",
		 1 : "http://cs61b.ug/sp16/",
		 2 : "https://github.com",
		 3 : "https://calcentral.berkeley.edu",
		 4 : "http://google.com"
		 }

def chrome(url):
	webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
print("Enter a url or enter a number of your top sites")
print()
for x in bookmark:
	print(x)
print()	
print("- " * 20)
print()
for x in homework:
	print(x)
print("=" * 40)
print()
url = input("Enter a url" + "\n")

print(sites.keys())



if (url in sites.keys()):
	sites[url]

	# if x == "0":
	# 	chrome("http://google.com")
	# elif x == "1":
	# 	chrome("http://cs61b.ug/sp16/")
	# elif x == "2":
	# 	chrome("https://github.com")
	# elif x == "3":
	# 	chrome("https://calcentral.berkeley.edu")
	# elif x == "4":
	# 	chrome("http://www.irchelp.org/irchelp/irctutorial.html")



	# elif x == "q":
	# 	chrome("http://cs61b.ug/sp16/materials/proj/proj0/proj0.html")
	# elif x == "w":
	# 	chrome("https://math.berkeley.edu/~apaulin/1Bhome1.pdf")	
else: 
	chrome(url)
print("\n" + "~I can't go there~")