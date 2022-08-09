from django.shortcuts import render, redirect

# Create your views here.

from .forms import KnihaForm
from .models import Kniha

def pridat_knihu(request):
    if request.method == "POST":
        formular = KnihaForm(request.POST)

        if formular.is_valid():
            formular.save()
            return redirect("dekuji")
    else:    
        formular = KnihaForm()
    return render(request, "knihy\pridat.html", {
        "form": formular
    })


def dekuji(request):
    return render(request, "knihy\dekuji.html")

# view funkce
# class based views - views založené na třídách