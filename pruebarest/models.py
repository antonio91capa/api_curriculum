from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20, null=False, blank=True)
    body = models.TextField(max_length=100, null=False, blank=True)
    date_published = models.DateTimeField(
        auto_now_add=True, verbose_name="date published"
    )
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title
