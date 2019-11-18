from django.db import models

# Create your models here.
class City (models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name
# for the plural words
    class Meta:
        verbose_name_plural ='cities'