from django.contrib import admin

# Register your models here.
from.models import GreenZone_Form

class smsHeartAdmin(admin.ModelAdmin):
    class Meta:
        model = GreenZone_Form

admin.site.register(GreenZone_Form, smsHeartAdmin)