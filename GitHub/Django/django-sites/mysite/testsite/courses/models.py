from django.db import models

# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'photo/%Y/%m/%d')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_add = models.BooleanField(default=True)


    def __str__(self):
        return self.title