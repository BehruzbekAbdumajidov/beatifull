from django.db import models

# Create your models here.

class Mahsulot(models.Model):
    nomi = models.CharField(max_length=20)
    bio = models.TextField()
    rasm = models.ImageField(upload_to='mahsulot/')
    narx = models.IntegerField()

    def __str__(self):
        return self.nomi


class Rasm(models.Model):
    nomi = models.CharField(max_length=40)
    bio = models.TextField()
    rasm = models.ImageField(upload_to='rasm/')

    def __str__(self):
        return self.nomi

class Haridor(models.Model):
    nomi = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='haridor/')
    bio = models.TextField()

    def __str__(self):
        return self.nomi

class Mol(models.Model):
    nomi = models.CharField(max_length=50)
    bio = models.TextField()
    rasm = models.ImageField(upload_to='mol/')

    def __str__(self):
        return self.nomi


