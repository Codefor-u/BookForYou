from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)

    def __str__(self):
        return self.title
    

class Profile(models.Model):
    username = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other fields as needed (e.g., bio, profile picture, etc.)

