from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=120, verbose_name="İSİM")
    subject = models.CharField(max_length=120, verbose_name="TELEFON")
    email = models.CharField(max_length=120, verbose_name="E-MAİL")
    phone = models.CharField(max_length=120, verbose_name="NOT")

    def __str__(self):
        return self.name


class Post2(models.Model):
    name = models.CharField(max_length=120, verbose_name="İSİM")
    subject = models.CharField(max_length=120, verbose_name="TELEFON")
    email = models.CharField(max_length=120, verbose_name="E-MAİL")
    phone = models.CharField(max_length=120, verbose_name="NOT")
    message = models.TextField(max_length=120, verbose_name="NOT")

    def __str__(self):
        return self.name


class Post3 (models.Model):
    name = models.CharField(max_length=120, verbose_name="İSİM")
    email = models.CharField(max_length=120, verbose_name="E-MAİL")
    phone = models.CharField(max_length=120, verbose_name="NOT")


    def __str__(self):
        return self.name
