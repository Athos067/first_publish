from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    nome = 'Wilson'
    lista_compras =['terno_branco','abotuaduras', 'mercenário']
    return render(request,'index.html',{'item' : nome, 'lista' : lista_compras})

def mostrar_sobre(request):
    return render(request,'sobre_html')    