from django.urls import path

from .views.lista_produto import lista_produto
from .views.criar_produto import criar_produto
from .views.atualizar_produto  import atualizar_produto

urlpatterns = [
    path('', lista_produto, name='lista_produto'),
    path('criar/produto/', criar_produto, name='criar_produto'),
    path('atualizar/produto/<int:index>/', atualizar_produto, name='atualizar_produto')

]
