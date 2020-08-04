import os
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


def image_path(instance, filename):
    """Generate file path for new cover image"""
    extension = filename.split('.')[-1]
    filename = f'{instance.slug}.{extension}'
    return os.path.join('upload/cover/', filename)


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
    slug = models.SlugField(max_length=255, unique=True)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    cover = models.ImageField(upload_to=image_path, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.slug)])

    def __str__(self):
        return self.title
