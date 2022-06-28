import csv 

with open("Class\PYTHON\Json-csv\data.csv") as infile:
    csv_file = csv.DictReader(infile, delimiter=",")
    for row in csv_file:
        print(row)
        print(f'Jmeno: {row["jmeno"]}, Firma:{row["pracoviste"]}, Plat:{row["plat"]}')