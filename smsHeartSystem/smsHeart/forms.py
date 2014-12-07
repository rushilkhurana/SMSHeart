__author__ = 'KellyAnn'

from django import forms
from django.utils import html

from .models import GreenZone_Form, YellowZone_Form, RedZone_Form

MEDICATIONS =(('1','Med'),('2','Advair Diskus'),('3','Advair HFA'),('4','Budesonide (Pulmicort)'),('5','Fluticasone (Flovent Diskus)'),('6','Fluticasone (Flovent HFA)'),('7','Mometasone (Asmanex) Twisthaler'),('8','Montelukast (Singulair)'),('9','Pulmicort Turbuhaler'),('10','Symbicort HFA'))
MEDUSAGE = (('1','How much'),('2','0.5mL'),('3','1 capsule'),('4','1 click'),('5','1 inhalation'),('6','1 puff'),('7','1 spray'),('8','2 capsules'),('9','2 clicks'),('10','2 inhalations'),('11','2 puffs'),('12','2 sprays'))
MEDTIMES = (('1','How often'), ('2', 'Every Morning'), ('3','Every Night'), ('4','Once per day'), ('5','Twice per day'))

YELLOWMEDICATIONS = (('1','Med'),('2','Albuterol'),('3','Beclomethasone (Qvar) HFA'),('4','Ipatropium (Atrovent)'),('5','Levalbuterol (Xoponex)'),('6','Levalbuterol HFA'),('7','Pro-Air (Albuterol) HFA'),('8','Proventil (Albuterol) HFA'),('9','Ventolin (Albuterol) HFA'))
YELLOWMEDUSAGE = (('1','How much'),('2','Dose'),('3','2 puffs'),('4','4 puffs'),('5','6 puffs'),('6','1 nebulizer treatment'))
YELLOWMEDTIMES = (('1','How often'),('2','Every 4 hours'))

REDMEDTIMES =(('1','How often'),('1','Every 20 minuets (Max 40 mins)'))

class GreenZone_Form(forms.ModelForm):

    symptomsCheck = forms.BooleanField(True)
    usualActivities = forms.BooleanField(False)
    addNewText = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add New'}))
    medOneNameList = forms.ChoiceField(choices=MEDICATIONS,widget=forms.Select(attrs={'class': 'form-control'}))
    medOneUsage = forms.ChoiceField(choices=MEDUSAGE,widget=forms.Select(attrs={'class': 'form-control'}))
    medOneTimes = forms.ChoiceField(choices=MEDTIMES,widget=forms.Select(attrs={'class': 'form-control'}))
    medTwoNameList = forms.ChoiceField(choices=MEDICATIONS,widget=forms.Select(attrs={'class': 'form-control'}))
    medTwoUsage = forms.ChoiceField(choices=MEDUSAGE,widget=forms.Select(attrs={'class': 'form-control'}))
    medTwoTimes = forms.ChoiceField(choices=MEDTIMES,widget=forms.Select(attrs={'class': 'form-control'}))
    specialInstruction = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = GreenZone_Form
        fields = ['symptomsCheck', 'usualActivities', 'addNewText','medOneNameList','medOneUsage','medOneTimes','medTwoNameList','medTwoUsage','medTwoTimes', 'specialInstruction']



class YellowZone_Form(forms.ModelForm):

    yellowSymptomsCheck = forms.BooleanField(True)
    yellowUsualActivities = forms.BooleanField(False)
    yellowUsualActivities2 = forms.BooleanField(False)
    yellowAddNewText = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add New'}))
    yellowMedOneNameList = forms.ChoiceField(choices=YELLOWMEDICATIONS,widget=forms.Select(attrs={'class': 'form-control'}))
    yellowMedOneUsage = forms.ChoiceField(choices=YELLOWMEDUSAGE,widget=forms.Select(attrs={'class': 'form-control'}))
    yellowMedOneTimes = forms.ChoiceField(choices=YELLOWMEDTIMES,widget=forms.Select(attrs={'class': 'form-control'}))
    yellowMedTwoNameList = forms.ChoiceField(choices=YELLOWMEDICATIONS,widget=forms.Select(attrs={'class': 'form-control'}))
    yellowMedTwoUsage = forms.ChoiceField(choices=YELLOWMEDUSAGE,widget=forms.Select(attrs={'class': 'form-control'}))
    yellowMedTwoTimes = forms.ChoiceField(choices=YELLOWMEDTIMES,widget=forms.Select(attrs={'class': 'form-control'}))
    yellowSpecialInstruction = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = YellowZone_Form
        fields = ['yellowSymptomsCheck', 'yellowUsualActivities','yellowUsualActivities2','yellowAddNewText','yellowMedOneNameList','yellowMedOneUsage','yellowMedOneTimes','yellowMedTwoNameList','yellowMedTwoUsage','yellowMedTwoTimes', 'yellowSpecialInstruction']

class RedZone_Form(forms.ModelForm):

    redSymptomsCheck = forms.BooleanField(True)
    redSymptomsCheck2 = forms.BooleanField(False)
    redSymptomsCheck3 = forms.BooleanField(False)
    redAddNewText = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add New'}))
    redMedOneNameList = forms.ChoiceField(choices=YELLOWMEDICATIONS,widget=forms.Select(attrs={'class': 'form-control'}))
    redMedOneUsage = forms.ChoiceField(choices=YELLOWMEDUSAGE,widget=forms.Select(attrs={'class': 'form-control'}))
    redMedOneTimes = forms.ChoiceField(choices=REDMEDTIMES,widget=forms.Select(attrs={'class': 'form-control'}))
    redMedTwoNameList = forms.ChoiceField(choices=YELLOWMEDICATIONS,widget=forms.Select(attrs={'class': 'form-control'}))
    redMedTwoUsage = forms.ChoiceField(choices=YELLOWMEDUSAGE,widget=forms.Select(attrs={'class': 'form-control'}))
    redMedTwoTimes = forms.ChoiceField(choices=REDMEDTIMES,widget=forms.Select(attrs={'class': 'form-control'}))
    redSpecialInstruction = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = RedZone_Form
        fields = ['redSymptomsCheck', 'redSymptomsCheck2', 'redSymptomsCheck3','redAddNewText','redMedOneNameList','redMedOneUsage','redMedOneTimes','redMedTwoNameList','redMedTwoNameList','redMedTwoUsage', 'redSpecialInstruction']