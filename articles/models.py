from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images/', blank=True, default='images/default.jpg')
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)  # Автогенерация slug
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title
        
    def snippet(self):
        return self.body[0:50] + '...'
