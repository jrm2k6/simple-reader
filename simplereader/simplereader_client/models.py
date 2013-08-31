from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feed(models.Model):
    title = models.CharField(max_length=300)
    url = models.URLField(max_length=500)
    date_added = models.DateField(True)
    category = models.CharField(max_length=300)

    def __unicode__(self):
        return self.title + ',' + str(self.url)

class ReaderUser(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField()

    def __unicode__(self):
        return self.user.first_name + ',' + str(self.email)
