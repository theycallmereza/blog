from django.db import models


# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = {
        ('published', 'Published'),
        ('draft', 'Draft')
    }
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
