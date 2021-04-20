import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


class Story(models.Model):
    title_text = models.CharField(max_length=100)
    body_text = models.CharField(max_length=250, default="body")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title_text
        return self.body_text



