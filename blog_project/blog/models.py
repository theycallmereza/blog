from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = {
        ('published', 'Published'),
        ('draft', 'Draft')
    }
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
