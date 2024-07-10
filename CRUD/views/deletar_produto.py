from django.shortcuts import redirect
from CRUD.models import Produto

def deletar_produto(request, index):

    Produto.objects.filter(index = index).delete()
    
    return redirect('lista_produto')