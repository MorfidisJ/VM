

import pyshorteners

link = input("Enter your link : ")

short = pyshorteners.Shortener()
x = short.tinyurl.short(link)

print("Shorted link is : "+x)