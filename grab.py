import requests as r
import os, sys
from bs4 import BeautifulSoup

os.system("clear")

#Banner
banner = """
==========================
Author : HexaKun
WhatsApp : 082335757008
==========================
"""
print banner

#Input Pengguna
From = int(raw_input("From : "))
To = int(raw_input("End Page : "))


for x in range(From, To+1):
   #Data
   api = "https://zone-f.org/mirror/detail/"
   url = api + str(x)
   #Requests Ke Web
   req = r.get(url)
   s = BeautifulSoup(req.content, "html.parser")
   link = s.find_all("p")[7].get_text()
   print link
   opn = open("finish.txt", "a")
   opn.write(link+"\n")
