#about disc direct

#dva typy cest - relativni a absolutni
"C:\\Users\\Admin\\Desktop\\python 2 podzim\\02-21\\priklad"

"/usr/admin/desktop/python 2/02-21"

# relativni cesta na win:(od adresare kde prave jsem)
"static\\obrazky\\more.jpg"

import os
from posixpath import dirname

os.path.sep
moje_cesta=os.path.join("Users","admin","Desktop")
print(moje_cesta)

moje_cesta_2 = os.path.join("C:\\","Users","admin","Desktop")
os.path.isabs(moje_cesta)

os.path.exists(moje_cesta_2)

os.path.isfile(moje_cesta_2)

os.path.isdir(moje_cesta_2)

os.getcwd()

os.curdir

os.pardir

os.chdir(os.pardir)

os.chdir("..")


os.chdir(os.join("Admin","Desktop"))

os.listdir()

import os
os.makedirs("adr")

import os
os.makedirs(os.path.join("adr","adr1","adr2"))
os.chdir(os.path.join("adr","adr1","adr2"))
os.listdir(os.curdir)

os.chdir(os.path.join("..","..",))

cesta = os.path.join("adr1","soubor.txt")
os.path.isfile(cesta)

os.path.abspath(cesta)
os.path.realpath("C:\\")

os.path.basename(cesta)
os.path.dirname(cesta)
os.path.split(cesta)

os.path.splitext(cesta)

os.path.getsize(cesta)
import os
import shutil
cesta = os.getcwd()

cesta_2 = "here.txt"
shutil.copy(cesta,cesta_2)

shutil.move("here.txt","tady.txt")

os.unlink("ahoj.txt")

os.rmdir("abc")

shutil.rmtree("abcd")
import os

for path,dirnames,filnames in os.walk(os.curdir):
    print("cesta je " + path)
    print("Adresare jsou " + str(dirnames))
    print("Soubory jsou " + str(filnames))