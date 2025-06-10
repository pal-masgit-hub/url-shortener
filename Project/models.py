from django.db import models

# Create your models here.

#
# class LongUrl(models.Model):
#     URL = models.CharField(max_length=500)


class ShortUrl(models.Model):
    source_url = models.CharField(max_length=3000, null=True, blank=True, unique=True)
    URL = models.CharField(max_length=100, null=True, blank=True, unique=True)

    # def __str__(self):
    #     return self.source_url
