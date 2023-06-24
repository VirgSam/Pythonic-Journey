from django.db import models

# Create your models here.

class Location(models.Model):
    name= models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name} ({self.address})"

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description= models.TextField()
    image= models.ImageField(upload_to="images", height_field=None, width_field=None, max_length=None)
    location=models.ForeignKey(Location)

    def __str__(self):
        return f"{self.title}"
    