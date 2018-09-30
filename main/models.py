from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Home(models.Model):
    hero_tag = models.TextField(max_length=200)
    hero_subtag = models.TextField(max_length=200)

    heading2 = models.TextField(max_length=200)
    heading2_description = models.TextField(max_length=500)

    # col-3 content
    col1 = models.CharField(max_length=50)
    col2 = models.CharField(max_length=50)
    col3 = models.CharField(max_length=50)

    # showcase 4 items
    showcase_heading = models.CharField(max_length=100)
    item1 = models.CharField(max_length=100)
    item2 = models.CharField(max_length=100)
    item3 = models.CharField(max_length=100)
    item4 = models.CharField(max_length=100)

    # Services container
    service_heading = models.CharField(max_length=100)
    service_description = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "Home Page"
    def __str__(self):
        return self.hero_tag
