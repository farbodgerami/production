from django.contrib import admin

from .models import *
 
class Wordsr(admin.ModelAdmin):
    list_display=['id','kalame','maani','description','lesson','audiofile']
admin.site.register(Word,Wordsr)

 

class levelstr(admin.ModelAdmin):
    list_display=['id','user','level',  ]
admin.site.register(Levelstring,levelstr)

 