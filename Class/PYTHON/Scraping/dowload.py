import requests
import os

url = "https://www.zoohit.cz/magazin/wp-content/uploads/2020/02/Francouzsk%C3%BD-buldo%C4%8Dek-768x512.jpg"

filename, file_extension = os.path.splitext(url)
r = requests.get(url)

with open ('subscribe2'+file_extension, 'wb') as f:
    f.write(r.content)