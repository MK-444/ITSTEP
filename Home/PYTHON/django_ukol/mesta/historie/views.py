from django.http import HttpResponse, Http404
from django import http 
from django.shortcuts import render


mesta = {
    "Praha": "je hlavni mesto Ceske republiky",
    "Charkov": "je druhe nejvetsi mesto v Ukrajine"
}

# Create your views here.
def index(request):
    context = {"mesto": mesta.keys()}
    return render (request, "historie\index.html", context)

def pocasi(request):
    context = {
        "popis_pocasi" : "Dnes je teplo priblizne 20 stupnu",
        "mnozstvi_srazek" :"Srazek dnes neni",
        "sila_vetru" : "Vitr taky neni?",
        "bude_dest": False
        }
    return render (request, "historie\pocasi.html", context)


def doprava(request):
    context = {
        "prujezdnost": True
    }
    return render(request, "historie\doprava.html", context)

def zajmavost(request, city):
    if city == "praha":
        return HttpResponse(f'<h2>Mesto {city} ma hodne zajmavosti ktere najdete na tento strance <a href="https://www.family.city/20-prazskych-nej-zajimavosti-o-praze-ktere-mozna-nevite/">https://www.family.city/20-prazskych-nej-zajimavosti-o-praze-ktere-mozna-nevite/</a></h2>')
    elif city == "charkov":
        return HttpResponse(f'<h2>Mesto {city} ma hodne zajmavosti ktere najdete na tento strance <a href="https://www.cklub.cz/pruvodce/ukrajina/charkov">https://www.cklub.cz/pruvodce/ukrajina/charkov</a></h2>')
    else:
        raise Http404("Spatne zadano mesto nebo mesto neexistuje")