from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
