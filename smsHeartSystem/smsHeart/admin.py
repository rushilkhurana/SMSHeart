from django.contrib import admin

# Register your models here.
from.models import smsHeart

class smsHeartAdmin(admin.ModelAdmin):
    class Meta:
        model = smsHeart

admin.site.register(smsHeart, smsHeartAdmin)