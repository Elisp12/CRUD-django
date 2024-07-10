from django.db import models

class Categoria(models.Model):
    index = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    index = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    descricao = models.TextField(max_length=500)
    categoria = models.ForeignKey(Categoria, models.CASCADE)

    def __str__(self):
        return self.nome 