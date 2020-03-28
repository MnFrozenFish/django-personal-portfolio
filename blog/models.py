from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField(max_length = 1500)
    date = models.DateField()

    def __str__(self):
        return self.title
