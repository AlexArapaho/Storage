from django.db import models
from django.contrib.auth.models import User

class Works(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='works/images/')

class Feedback(models.Model):
    title = models.CharField(max_length=70)
    feedback = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title