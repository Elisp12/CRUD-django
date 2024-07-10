from django.shortcuts import render, redirect

from CRUD.models import Categoria, Produto


def criar_produto(request):
    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')
    categoria = request.POST.get('categoria')

    if request.method == 'POST':
        Produto.objects.create(nome = nome, descricao = descricao, categoria = Categoria.objects.get(index = categoria))
        return redirect('lista_produto')
    
    lista_categoria = Categoria.objects.all()
    context = {
        'categoria': lista_categoria
    }
    return render(request, 'produto/formulario_produto.html', context = context)