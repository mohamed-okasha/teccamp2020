from django.db import models

# Create your models here.
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created =  models.DateField(default=timezone.now())
    due_date =  models.DateField(default=timezone.now())
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class  Meta:
        verbose_name_plural = 'Todos'

    def __str__(self):
        return self.title