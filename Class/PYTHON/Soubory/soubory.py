import os


os.getcwd() #current working directory

os.curdir #opet current directory, ale ted realative
#aktualni adresat = "."

os.pardir # parent directory
#rodicovsky adresar ".."


soubor = open("novy.txt", "r")
#mody pro otevirani souboru
#r - read(neni nutne psat, je to default)
#w - write
#a - append

obsah_souboru = soubor.read()
obsah_souboru_jako_list = soubor.readlines()
print(obsah_souboru_jako_list)
soubor.close()


soubor2 = open("novy7.txt", "w")
soubor2.write("ahoj\n")
soubor2.write("dobry den\n")
soubor2.write("jak se mate\n")
soubor2.close()


soubor3 = open("novy7.txt", "a")
soubor3.write("Tohle je ctvrty radek souboru")
soubor3.close()


soubor_pro_cteni = open("novy7.txt")
print(soubor_pro_cteni.read())
soubor_pro_cteni.close()