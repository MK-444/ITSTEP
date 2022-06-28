from multiprocessing import context
from urllib import response
from django import http
from django.shortcuts import render
from django.http import HttpResponse, Http404


nase_zvirata = {
    "krtek": "Krtek zije pod zemi.",
    "opice": "Opice maji rady banany.",
    "hroch": "Hroch je velky zabijak.",
    "pes": "Pes rad steka.",
    "pstros": "Pstros je ptak, ale neleta."
    
}
# konce databaze

# Create your views here.
def index(request):
    context = {"zvirata": nase_zvirata.keys()}
    return render(request, "informace\index.html", context)
    #===========================================
    # response = "<h1>Hlavni stranka o zviratech.</h1>\n"
    # response += "<p>Metoda je " + request.method + "</p>\n"
    # response += "<ol>\n"
    # for zvire, popis in nase_zvirata.items():
    #     response += f'<li><a href="informace/{zvire}">{zvire}</a>- {popis}</li>\n'
    # response += "</ol>"
    #====================================================
    

def slon(request):
    context = {
        "jmeno":"Jumbo",
        "barva": "ruzova",
        "povolani": "strikat na lidi vodu",
        "je_hezky": False,
    }
    return render(request, "informace\slon.html", context)
    #     "jmeno":"Jumbo",
    #     "barva": "ruzova",
    #     "povolani": "strikat na lidi vodu"
    # })

def zirafa(request):
    context = {
        "slovo": "nosorozec",
        "text": "hrock je moje oblibene zvire",
        "angl_slovo": "dog",
        "pocet_psu": 1,
        "cislo": 57,
        "cislo_jako_string": "57",
        "je_hezky": True,
        "je_hezky2": False,
        "je_hezky3": None,
        "seznam": ["pes", "kocka", "mys"],
        "s2": [4,5,6],
        "s3": [7,8,9]
    }
    return render(request, "informace\zirafa.html", context)

#DTL = Django template language


def informace(request, zvire):
    popis = nase_zvirata[zvire]
    return render(request, "informace\popis.html", {
        "zvire": zvire,
        "popis": popis 
    })
#DIL = Django template language
