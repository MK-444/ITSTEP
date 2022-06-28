string = "slon je modry, ma chobot a kly. Zije v Inii a Africe."
lists = [list.strip(' ') for list in string]
print(lists)

position = string.index("chobot")
print(position)



"""
? - 0x - 1x znak předtím
+ - 1x - nekonečnokrát znak předtím
* - 0x - nekonečnokrát znak předtím
| - nebo
\d - číslice
\w - číslice, písmeno nebo podtržítko
\s - bílý znak (mezera, tabulátor nebo nový řádek)
\b - hranice slova
^ - začátek řetězce
$ - konec řetězce
() - skupina
{} - kolikrát je ten znak předtím
[] - výčet (tj. cokoliv ze znaků v závorkách)
[^] - výčet, ale negace (tj. cokoliv kromě znaků v závorkách)
"""

#3. find(), index, rfind, rindex

#4. documentace, stackoverflow



#REGULARNI VYRAZY
#REGEX = REGULARNI VYRAZY
from logging import exception
import re

"""
retezec = "Slon je sedivy, ma chobot a kly. Jeho telefon je 77755-123456 Zije v Africe"
print(retezec.find("chobot"))

regex = re.compile(r"((abc){4})-?(\d{6,10}")
vysledek = regex.search(retezec)
print(f"Prevolba je {vysledek.group(1)}")
print(f"Samotne cislo je {vysledek.group(2)}")
print(f"Cele tel. cislo je {vysledek.group()}")
print(f"Cele tel. cislo je {vysledek.group(0)}")

"""

ret2 = "U nas bydli zelepravony prvo"
regex2 = re.compile(r"pra?vo")
vysledek = regex2.search(ret2)
print(vysledek.group())
ret3 = "Mame doma modry plot."

regex3 = re.compile(r"jablko|hrusky")
regex4 = re.compile(r"plo(d|t)")



regex_exercise_1 = "eglefrfl4clevjkbkleddfwles"
regex_compile = re.compile(r"le(s|d|v)")
answer =  regex_compile.search(regex_exercise_1)




regex_exercise_2 = "eglhradevjkbkleddfhadwles"
regex_compile2 = re.compile(r"h(|r)ad")
answer2 = regex_compile2.search(regex_exercise_2)
print(answer2.group())


# regex_exercise_3 = "sfdszahrada sfdhpodhrada dhfdohrada"
# regex_compile3 = re.compile(r"(za|o|pod)?hrad")
# answer3 = regex_compile3.split(regex_exercise_3)
# print(answer3.group())

regex_exercise_4 = "spravedlnost, nost, hrdost, pronost"
regex_compile4 = re.compile(r"(\w*nost\b)")
answer4 = regex_compile4.findall(regex_exercise_4)
print(answer4)


# #5 regex
# text = "Slon je modry. Ma telefon: jeho telefon je 555. Je hezky, vsichni navstevnici ho maji radi. Je z Afriky; mohl by byt i y Indie. Nas slon se jmenuje slono.bobo."
# import re
# muj_regex = re.compile(r"[;,:.]\s")
# roztrhany_text = muj_regex.split(text)
# print(roztrhany_text)


# #6 regex 
# regex_exercise_6 = "televize, telefon, jablko, mic, mys"
# regex_compile6 = re.compile(r"A-Za-z{7,}")
# answer6 = regex_compile6.findall(regex_exercise_6)
# print(answer6)


# #7 regex
# regex_exercise_7 = "Okno, mic, okno, kase"
# regex_compile7 = re.compile(r"\b[^oO\s]+\b")
# answer7 = regex_compile6.findall(regex_exercise_7)
# print(answer7)

regex_exercise_8 = "+420 234-232-222 +420 2034-232-222"
regex_compile8 = re.compile(r"(\+420)\d{3}-\d{3}-\d{3}\b")
answer8 = regex_compile8.findall(regex_exercise_8)
print(answer8)



