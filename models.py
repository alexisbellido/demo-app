from django.urls import reverse
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title


class TVProgram(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('demo:tv-program-detail', args=(self.id,))
