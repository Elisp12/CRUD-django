from django.shortcuts import render, redirect
from CRUD.models import Categoria, Produto

def atualizar_produto(request, index):
    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')
    categoria = request.POST.get('categoria')

    produto = Produto.objects.filter(index = index)

    if request.method == 'POST':
        Produto.objects.filter(index = index).update(nome = nome, descricao = descricao, categoria = Categoria.objects.get(index = categoria))
        return redirect('lista_produto')

    lista_categoria = Categoria.objects.all()

    context = {
        'categoria': lista_categoria,
        'produto': produto
    }
    return render(request, 'produto/atualizar_produto.html', context = context)
