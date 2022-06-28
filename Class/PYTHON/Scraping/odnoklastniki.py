import requests
from bs4 import BeautifulSoup
import os

url = "https://ok.ru/profile/330185714638/photos"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
#print(soup.prettify())
photo_group = soup.find_all("div", class_="ugrid_cnt")
print(photo_group)
# #============================
# ul_photo =  photo_group.find_all("ul", class_="ugrid_cnt")
# # print(ul_photo)
# #============================
# li_photo = ul_photo.find("li", class_="ugrid_i")

# link = "https:"
# for photo in li_photo:
#     # print(photo.prettify())
#     a_photo = photo.find("a", class_="photo-card_cnt").find("img", class_="rotate__0deg")
#     print(link + a_photo["src"])

    