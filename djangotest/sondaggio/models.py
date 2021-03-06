from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Domanda(models.Model):
    testo_domanda = models.CharField(max_length = 200)
    data_pub = models.DateTimeField('pubblicata il')

    def __str__(self):
    	return self.testo_domanda

    def pubblicata_di_recente(self):
    	now = timezone.now()
    	return (self.data_pub >= now - datetime.timedelta(days = 30)) and (self.data_pub < now)


class Scelta(models.Model):
    domanda = models.ForeignKey(Domanda, on_delete = models.CASCADE)
    testo_scelta = models.CharField(max_length = 200)
    voto = models.IntegerField(default = 0)