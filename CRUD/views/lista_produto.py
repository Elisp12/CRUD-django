from django.shortcuts import render

from CRUD.models import Produto

def lista_produto(request):
    l_produto = Produto.objects.all()

    context = {
        'lista_produto': l_produto
    }
    return render(request, 'produto/lista-produto.html', context= context)