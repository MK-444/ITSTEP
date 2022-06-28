from django.shortcuts import render, redirect
from django.views import View
from .models import Kniha 
from .forms import KnihaForm
from django.views.generic import TemplateView 
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
#==================== Nova Kniha =========================
class NovaKniha2(LoginRequiredMixin, FormView):
    form_class = KnihaForm 
    template_name = "knihy/nova_kniha.html"
    success_url = "dekuji"
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# class NovaKniha(View):
#     def post(self, request):
#         form = KnihaForm(request.POST)
#         if form.is_valid():
#             form.save()
#         context = {"form": form}
#         return redirect("podekovani")
    
#     def get(self, request):
#         form = KnihaForm()
#         context = {"form": form}
#         return render(request, "knihy/nova_kniha.html", context)
    

# def nova_kniha(request):
#     if request.method == "POST":
#         form = KnihaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("podekovani")
#     else:
#         form = KnihaForm()
#     context = {"form": form}
#     return render(request, "knihy/nova_kniha.html", context)


    # def my_render(self, request, form):
    #     context = {"form": form}
    #     return render(request, "knihy/nova_kniha.html", context)
    
    # jmeno = form.cleaned_data["jmeno"]
    # autor = form.cleaned_data["autor"]
    # recenze = form.cleaned_data["recenze"]
    # nova_kniha = Kniha(jmeno=jmeno, autor=autor, recenze=recenze)
    # nova_kniha.save()

#==================== Dekuji =========================
def dekuji(request):
    return render(request, "knihy/dekuji.html")

# class Dekuji(TemplateView):
#     template_name = "knihy/dekuji.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["jmeno_slona"] = "Jumbo"
#         return context
    
#==================== Seznam =========================

def seznam(request):
    knihy = Kniha.objects.all()
    posledni = request.session.get("posledni", "zadna")
    return render(request, "knihy/seznam.html", {"knihy": knihy})

# class Seznam(TemplateView):
#     template_name = "knihy/seznam.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         knihy = Kniha.objects.all()
#         context["knihy"] = knihy
#         return context
    
# class Seznam2(ListView):
#     model = Kniha 
#     template_name = "knihy/seznam.html"
#     context_object_name = "knihy"
#     #queryset = Kniha.objects.all()[35:]
    
#==================== Detail =========================
@login_required
def detail(request, pk):
    kniha  = Kniha.objects.get(pk=pk)
    request.session["posledni"] = kniha.jmeno
    return render(request, "knihy/detail.html", {"kniha": kniha})

# class Detail(DetailView):
#     model = Kniha
#     template_name = "knihy/detail.html"
    
    
#     if request.method == "POST":
#         print("Formular bal odeslan....")
#         jmeno_nove_knihy = request.POST["jmeno"]
#         if jmeno_nove_knihy != "":
#             nova_kniha = Kniha(jmeno=jmeno_nove_knihy)
#             nova_kniha.save()
#             return redirect("podekovani")
