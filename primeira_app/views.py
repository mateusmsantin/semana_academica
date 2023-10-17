from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


#
from django.views.generic.edit import CreateView

#def cadastrar_usuario(request):
#    return render(request, "primeira_app/form.html")


from django.shortcuts import render, redirect
from .forms import *

#def cadastrar_usuario(request):
#    form = UsuarioForm()
#    return render(request, "primeira_app/form.html", {'form':form})

def cadastrar_usuario(request):
    if request.method=='POST':
        saverecord=Usuario()
        saverecord.nome=request.POST.get('nome')
        saverecord.email=request.POST.get('email')
        saverecord.sexo=request.POST.get('sexo')
        saverecord.save()
        return redirect("/")
        
    
    if request.method=='GET':
        print('VEIO PELO GET')
        form = UsuarioForm()

    return render(request, "primeira_app/form.html", {"form":form})
