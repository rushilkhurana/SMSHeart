__author__ = 'KellyAnn'

from django import forms

from .models import smsHeart

class PatientForm(forms.ModelForm):
    class Meta:
        model = smsHeart

# class IBaapForm(forms.ModelForm):
#     class Meta:
#         model = smsHeartIbbap