import requests
from bs4 import BeautifulSoup 


url = "https://www.expats.cz/jobs/offers/it-itc"

response = requests.get(url)
#1
soup = BeautifulSoup(response.content, "html.parser")

main_content = soup.find(id="jobs-index")
# print(type(main_content))
# print(main_content.prettify())
header = main_content.find("div", class_="list-header")
# print(type(header))
# print(header.prettify())

anchor = header.find("a")
print(anchor.text)
print(type(anchor.text))
#2
jobs = main_content.find(class_="job-list")

all_jobs = jobs.find_all("article")

print(type(all_jobs))
print(all_jobs)
links = "https://www.expats.cz/"
for job in all_jobs:
    anchor = job.find("h3").find("a")
    print(anchor.text)
    print(links + anchor["href"])
    
#-----------------------------------------------------------------------------------------------------------
#url = "https://api.github.com/user"
#url = "https://twitter.com/search?q=python&q=python"

#jen kontrola jestli nevznikla chyba
# response.raise_for_status()

# with open("soubor.html", "wb") as input:
#     input.write(response.content)
