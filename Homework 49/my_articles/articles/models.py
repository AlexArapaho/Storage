from django.db import models

class Articles(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    title_pic = models.ImageField(upload_to='articles/images/')
    art_text = models.TextField()

    def __str__(self):
        return self.title
