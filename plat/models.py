from django.db import models


# Create your models here.
class PlatModel(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.summary}"

    class Meta:
        verbose_name = "Plat"
        verbose_name_plural = "Plats"
