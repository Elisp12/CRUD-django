from django.urls import path

from .views.lista_produto import lista_produto

urlpatterns = [
    path('', lista_produto, name='lista_prouto')
]
