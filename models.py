from django.db import models

class Burger(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='img')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
