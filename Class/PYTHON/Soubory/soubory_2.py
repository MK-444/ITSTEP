# soubor = open("5-minutovka.py", "r")
with open("novy.txt", "r") as soubor:
    for radek in soubor:
        radek = radek.strip("\n")
        if radek.endswith("radek"):
            print(radek, end="")

#with = context manager, ktery se postara o zavreni souboru



with open("datove_struktury.txt") as file:
    for line in file:
        with open("copy_file.txt", "w") as new_file:
            new_file.write(line)
            print(new_file)

        