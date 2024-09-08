from django.db import models
from django.contrib.auth.models import User

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
