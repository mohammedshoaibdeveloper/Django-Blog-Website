from django.db import models

# Create your models here.
class  Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=130)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title +  ' written by ' + self.author_name 