from django.db import models

# Create your models here.
class Conselho(models.Model):
    pedagogo = models.CharField(max_length=20)
    dia = models.DateField(auto_now=False, auto_now_add=False);
    classe = models.CharField(max_length=20)
    ata = models.TextField()
    class Meta:
        verbose_name_plural = "Conselhoes"