from django.db import models

class Contenido(models.Model):
    contenido_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    episodios = models.IntegerField()

    class Meta:
        db_table = 'contenido'

    def __str__(self):
        return self.titulo