import os

from django.db import models

# Create your models here.
from app.settings import BASE_DIR


class Header(models.Model):
    name = models.CharField(max_length=30)
    width = models.IntegerField()
    order = models.IntegerField()

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Имя',
                            null=True, )
    file = models.FilePathField(path=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                # recursive=True,
                                # allow_files=True,
                                # allow_folders=True,
                                verbose_name='Файл')

    def __str__(self):
        return self.name
