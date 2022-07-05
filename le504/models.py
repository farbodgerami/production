from os import truncate
from django.db import models
from users.models import *
from django.db.models.signals import post_save,pre_save
from ckeditor_uploader.fields import RichTextUploadingField
import json
def validatefileextension(value):
    import os
    from django.core.exceptions import ValidationError
    ext=os.path.splitext(value.name)[1]
    validextention=['.mp3','.wav','.mpeg']
    if not ext.lower() in validextention:
        raise ValidationError('unsupported file extension')

class Word(models.Model):
    kalame=models.CharField(max_length=300,null=True,blank=False)
    maani=models.CharField(max_length=300,null=True,blank=True )
    description= RichTextUploadingField(null=True,blank=True)
    lesson=models.IntegerField( default=1,blank=False,null=False)
    audiofile = models.FileField(blank=True,null=True,upload_to='504audio/',validators=[validatefileextension] )
    def __str__(self):
        return self.kalame
        
    def delete(self, *args, **kwargs):
     if self.audiofile:
        self.audiofile.delete()
     super().delete(*args, **kwargs)
 

class Levelstring(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    level=models.TextField(default="{}",blank=False,null=False)

def createlevelarraydependonuser(sender,**kwargs):
    words=Word.objects.all()
    a={}
 
    if kwargs['created']:      
        for i in words:
             a.update({i.id: 1})
        levelstring=Levelstring()
        levelstring.user=kwargs['instance']
        levelstring.level=json.dumps(a)
        levelstring.save()
post_save.connect(createlevelarraydependonuser,sender=User)

 

def createlevelarraydependonword(sender,**kwargs):
    users=User.objects.all()
    
    if kwargs['created']:      
        for i in users:        
            userlevelstring=Levelstring.objects.get(user_id=i.id)
            # string to json
            res = json.loads(userlevelstring.level)
            res.update({kwargs['instance'].id: 1})
            # json to string
            userlevelstring.level = json.dumps(res)
            userlevelstring.save()
            
post_save.connect(createlevelarraydependonword,sender=Word)

# def createlevelarraydependonuser(sender,**kwargs):
#     words1100=Word1100.objects.all()
#     if kwargs['created']:      
#         Level1100.objects.bulk_create([Level1100(user1100=kwargs['instance'],word1100=i) for i in words1100 ])
# post_save.connect(createlevelarraydependonuser,sender=User1100)
 
# def createlevelarraydependonword(sender,**kwargs):
#     users1100=User1100.objects.all()
#     if kwargs['created']:      
#         Level1100.objects.bulk_create([Level1100(word1100=kwargs['instance'],user1100=i) for i in users1100 ])
# post_save.connect(createlevelarraydependonword,sender=Word1100)

# ba zadane yek dokme dar react n ta kalame be n ta user ezafe mishe:
# def createlevelarraydependonuser(sender,**kwargs):
#     users=[userr1,userr2,...]
#     for userr in users:
#         words=[word1,word2,...]
#         Level.objects.bulk_create([Level(user=userr,word=i) for i in words ])
 
 

 