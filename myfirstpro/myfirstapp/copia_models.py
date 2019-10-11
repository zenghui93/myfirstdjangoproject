from django.db import models
from django.forms import ModelForm
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class List(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Record(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name="category_set", on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    list = models.ForeignKey(List, related_name="records", on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='photos/', blank=True)
    submission_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
