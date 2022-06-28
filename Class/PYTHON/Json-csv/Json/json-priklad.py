import json
from textwrap import indent


data = {
    "jmeno": "Maria",
    "vek": 17,
    "cislo": 25.0,
    "sporty": ["fotbal", "basketbal", "hokej"],
    "pije mleko": True,
    "znamky": (1,2,3,4,5),
    "domaci zvire":{
        "jmeno": "Nika",
        "rasa": "francouzsky buldog",
        "povolani":"hlidac"
    }
}

with open("data.json", "w") as infile:
    json.dump(data, infile, indent=4) #dump do souboru (save)
    
retezec = json.dumps(data, indent=4) #dumps do retezce (stringu)
print(retezec)
