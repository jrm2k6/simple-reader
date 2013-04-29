from django.db import models

# Create your models here.
class Feed(models.Model):
    title = models.CharField(max_length=300)
    url = models.URLField(max_length=500)
    date_added = models.DateField(True)
    category = models.CharField(max_length=300)

    def __unicode__(self):
        return self.title + ' ::' + str(self.url)

class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name + ' ::' + str(self.email)