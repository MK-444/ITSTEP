"""
hele komentar
jeste jeden komentar
dalsi komentar
"""



retezec = r"ahoj \trava"
#escape sekvence

#\n novy radek
#\t tabulator

# s R na zacatku = raw string = escape sekvence ztraci vyznam
print(retezec)

jiny_retezec = """hura trojite uvozovky"""
jeste_jiny_retezec = '''radek
dalsi radek
jeste dalsi radek
'''

print(jeste_jiny_retezec)



vek = 25
jmeno = "Petr"
print(f"Moje jmeno je {jmeno} a je mi {vek + 3}. To jsem mladej , co?: ")

retezec = "ahoj dnes jsu jist"
seznam = [2,5,9,8]
print(retezec[2])

#STRINGY JSOU IMMUTABLE, TEDY NEMENE

seznam = "anicka ma rada jablko".split()
seznam = "***".join(seznam)
print(seznam)