from django.db import models
from django.utils.text import slugify
# Create your models here.



class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, default='')
    slug = models.SlugField(unique=True, blank=True, default='')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog_app:detial", args=[str(self.slug)])
    

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)