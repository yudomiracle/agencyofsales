from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.pk} - {self.category}'


class Home(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    info = models.TextField()
    s = models.FloatField()
    district = models.CharField(max_length=200)
    cost = models.IntegerField()

    def __str__(self):
        return self.title