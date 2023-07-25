from django.db import models

# Create your models here.
# Test model to run a docker container

class Sample(model.Models):
    attachment = models.FileField()