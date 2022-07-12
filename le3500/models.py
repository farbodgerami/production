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
    audiofile = models.FileField(blank=True,null=True,upload_to='3500audio/',validators=[validatefileextension] )
    def __str__(self):
        return self.kalame
        
    def delete(self, *args, **kwargs):
     if self.audiofile:
        self.audiofile.delete()
     super().delete(*args, **kwargs)
 

class Levelstring(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='levelstring3')
    level=models.TextField(default="{}",blank=False,null=False)
def createlevelarraydependonuserprofile(sender,**kwargs):
    # trycathch vase ine ke age levelstring vojood dasht dastesh nazan. agara vojood nadasht yeki jadid besaz
    try:
        userlevelstring=Levelstring.objects.get(user_id=kwargs['instance'].user.id)
      
    except:
        words=Word.objects.all()
        a={}
        userplanarray=kwargs['instance'].userplan.split(' ')
        if 'le3500' in userplanarray:    
            for i in words:
                a.update({i.id:{i.id: 1,"num":0}})
            levelstring=Levelstring()
            levelstring.user=kwargs['instance'].user
            levelstring.level=json.dumps(a)
            levelstring.save()
post_save.connect(createlevelarraydependonuserprofile,sender=Userprofile)

  
def createlevelarraydependonword(sender,**kwargs):
    levelstrings=Levelstring.objects.all()
    if kwargs['created']:      
        for i in levelstrings:        
            res = json.loads(i.level)
            res.update({kwargs['instance'].id:{kwargs['instance'].id: 1,"num":0}})
            # json to string
            i.level = json.dumps(res)
            i.save() 
post_save.connect(createlevelarraydependonword,sender=Word)