from django.db import models

class PhotoSubmission(models.Model):
    name = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to='photos/',null=True)
    date = models.CharField(max_length=100, null=True)
    time = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
