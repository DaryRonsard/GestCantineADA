from django.db import models
from plat.models import PlatModel


# Create your models here.
class MenuModels(models.Model):
    creation_date = models.DateField()
    platModel = models.OneToOneField(PlatModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Menu du {self.creation_date}"


    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"