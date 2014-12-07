from django.db import models
from django.forms import ModelForm

from django.utils.encoding import smart_unicode

# Create your models here.
class smsHeart(models.Model):
    firstName = models.TextField(100)

class GreenZone_Form(models.Model):
   symptomsCheck = models.BooleanField(True)
   usualActivities = models.BooleanField(False)
   addNewText = models.TextField()

class YellowZone_Form(models.Model):
   yellowSymptomsCheck = models.BooleanField(True)
   yellowUsualActivities = models.BooleanField(False)
   yellowUsualActivities2 = models.BooleanField(False)
   yellowAddNewText = models.TextField()

class RedZone_Form(models.Model):
   redSymptomsCheck = models.BooleanField(True)
   redUsualActivities = models.BooleanField(False)
   redUsualActivities2 = models.BooleanField(False)
   redUsualActivities3 = models.BooleanField(False)
   redAddNewText = models.TextField()

def __unicode__(self):
        return smart_unicode(self.email)


