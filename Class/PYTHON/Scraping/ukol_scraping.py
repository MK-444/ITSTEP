import requests 
from bs4 import BeautifulSoup 


url = "http://www.paluba.cz/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

wrap = soup.find("div", id="wrap")
row = wrap.find("div", class_="row")
col = row.find("div", class_="col-md-4")
title = col.find("h2")
print(title.text)
p = col.find_all("p")
for akce in p:
    a = akce.find("a")
    if a.has_key('href'):
        a['href']
        print(a)
    # a = akce.find("a")
    # print(a["href"])
    description = akce.text
    print(description)
    
