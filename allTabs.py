#!/usr/bin/python3
import webbrowser
import os
import sys

def addTab():
	file = open(path, "a")
	checker = "http"
	if len(sys.argv) == 2:
		if checker in sys.argv[1]:
			file.write(sys.argv[1]+ "\n")
			print("File Updated! " +sys.argv[1]+ " added.")
	else:	
		newTab = input("Enter URL to add: ")
		if checker in newTab:
			file.write(newTab+ "\n")
			print("File Updated! " +newTab+ " added.")
		else:
			print("Is this a URL? Does not contain " +checker+ " Try again.")
#--------------------Begin--------------------------
#Remove all irrevelant urls
'''
def chrome(url):
	webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
'''

path = "C:/Users/Alex/Projects/GoogSearch/recover.txt"
totalLines = 0
my_urls = []



if len(sys.argv) == 2:
	addTab()
	


else :
	cnt = 0
	file = open(path, "r+")
	for line in file:
		if line != "\n":
			my_urls.append(line)
			print("{} : {}".format(cnt, line))
			cnt += 1
			totalLines = totalLines + 1


	ans = ""
	while ans.lower() != "o" and ans.lower() != "a" and ans.lower() != "d" and ans.lower() != "x":
		ans = input("Open (O) | Add Entry (A) | Delete Entry (D) | Cancel (X): ")
		ans = ans.lower()
	
	if ans.lower() == "o":

		for line in my_urls:
			os.startfile(line)	

	elif ans.lower() == "a":
		file.close()
		addTab()

	elif ans.lower() == "d":
		file.close()
		file = open(path, "w+")
		ans = 999

		while (int(ans) > totalLines):
			ans = input("Enter Entry Num: ")
			ans = int(ans)
		print(my_urls.pop(ans) + "--= Removed =--")
		file.writelines(my_urls)
		
	elif ans.lower() == "x":
		ans = input("Press Enter to exit.")

	else:
		ans = input("Invalid option. Exiting.....press Enter")

	file.close()