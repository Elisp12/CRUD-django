from django.urls import path

from .views.lista_produto import lista_produto
from .views.criar_produto import criar_produto

urlpatterns = [
    path('', lista_produto, name='lista_produto'),
    path('criar/produto/', criar_produto, name='criar_produto')

]
