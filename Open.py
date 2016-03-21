#! /usr/bin/env python
#!/bin/sh
import os
import sys
import time
__author__ = 'Alex'


import webbrowser
core = [" 0) Google",
		 " 1) MAIN CS61B",
		 " 2) Github",
		 " 3) CalCentral",
		 " 4) IRC help",
		 " 5) CSM"
		]

later = [" q) Clamp Lamp"]

sites = {0 : "http://google.com",
		 1 : "http://cs61b.ug/sp16/",
		 2 : "https://github.com",
		 3 : "https://calcentral.berkeley.edu",
		 4 : "http://google.com",
		 5 : "http://csmberkeley.github.io/",

		 "q" : "http://www.amazon.com/Newhouse-Lighting-Energy-Efficient-Clamp-Light/dp/B00FIYJXAQ/ref=sr_1_1?s=lamps-light&ie=UTF8&qid=1454293018&sr=1-1&keywords=clamp+lights"
		 }

def chrome(url):
	webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
print("Enter a url or enter a number of your top sites")
print(sites.keys())
print()
for x in core:
	print(x)
print()
print("- " * 20)
print()
for x in later:
	print(x)
print("=" * 40)
print()
url = input("Enter a url || key" + "\n")


if "." in url:
	chrome(url)
elif (url in sites.keys()):
	chrome(sites[url])
elif (not isinstance(url, str) and int(url) in sites.keys()):
	chrome(sites[int(url)])
else: 
	print("Not sure what you're trying to put...\n ~~ Restarting... ~~")
	time.sleep(3)
	print()
	os.system("python Open.py")
