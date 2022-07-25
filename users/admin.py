from django.contrib import admin
from .models import *
# Register your models here.
class levelsr(admin.ModelAdmin):
    list_display=['id','username','email','is_admin','is_active' ]
admin.site.register(User,levelsr)

class userprofile(admin.ModelAdmin):
    list_display=['id','user','phonenumber' ]
admin.site.register(Userprofile,userprofile)

 