from django.db import models


class Book(models.Model):
    label = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    genre = models.CharField(max_length=30)

    class Meta:
        db_table = 'books'
        managed = True
