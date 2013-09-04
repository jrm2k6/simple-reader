import hashlib
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feed(models.Model):
    title = models.CharField(max_length=300)
    url = models.URLField(max_length=500)
    date_added = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=300)

    def __unicode__(self):
        return self.title + ',' + str(self.url)

class ReaderUser(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField()
    date_joined = models.DateField(auto_now_add=True)
    password = models.CharField(max_length=300)
    
    def save(self):
        self.password = hashlib.sha1(self.password).hexdigest()
        super(ReaderUser, self).save()
 
    def __unicode__(self):
        return self.first_name + ',' + str(self.email)
