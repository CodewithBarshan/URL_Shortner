from django.db import models

# Create your models here.

class ShortUrl(models.Model):
    original_url=models.URLField(max_length=7000)
    short_url=models.CharField(max_length=100)
    time_date_created=models.DateTimeField()

    def __str__(self):
        return self.original_url
        