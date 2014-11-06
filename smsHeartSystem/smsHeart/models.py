from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class smsHeart(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    birthdate = models.DateField()
    phone = models.CharField(max_length=10, null=True, blank=True)
    dustMites = models.BooleanField(None);
    cats = models.BooleanField(None);
    cigaretteSmoke = models.BooleanField(None);



    def __unicode__(self):
        return smart_unicode(self.email)


# class smsHeartIbbap(models.Model):



