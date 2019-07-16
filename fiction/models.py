from django.db import models

# Create your models here.


class fiction(models.Model):
    book_name = models.CharField(max_length=30)
    author_name = models.CharField(max_length=30)
    edition = models.IntegerField(max_length=50)
    release_date = models.DateField()  # for creating date column

'''
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=30)
    contact    = models.IntegerField()
    email      = models.EmailField(max_length=50)
    age        = models.IntegerField()  
'''