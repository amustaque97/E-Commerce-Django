from django.db import models
from datetime import datetime

# Create your models here.
class Products(models.Model):
    # product database
    product_title = models.CharField(max_length=200,unique=True)
    product_slug = models.SlugField(unique=True)
    product_image = models.TextField()
    product_quantity = models.PositiveIntegerField()
    product_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_title
