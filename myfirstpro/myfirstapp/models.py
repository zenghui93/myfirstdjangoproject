from django.db import models
from django.urls import reverse

from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class List(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Fruits(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
       return self.name 


class Record(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name="category_sets", on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    list = models.ForeignKey(List, related_name="list_sets", on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='photos/', default='photos/imagenotuploaded.jpg', blank=True)
    submission_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('class_record_detail', kwargs={'pk': self.pk})






