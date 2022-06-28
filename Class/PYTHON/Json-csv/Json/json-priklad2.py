import json 

with open("data.json") as infile:
    print(json.load(infile)) # load = precist
    
retezec = '{"jmeno": "Alik", "rasa": "bernardyn"}'


slovnik = json.loads(retezec)

print(slovnik)
print(slovnik["jmeno"])