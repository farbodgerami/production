
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import datetime
from django.db.models.signals import post_save
from datetime import date,timedelta
class UserManager(BaseUserManager):
    def create_user(self,email,username,password):
        if not email:
            raise ValueError('plz email')
        if not username:
            raise ValueError('plz user')
         
        user=self.model(email=self.normalize_email(email),username=username,)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username,password):
        user=self.create_user(email,username,password)
        user.is_admin=True
        # user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(unique=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    # vase superuser: 
    USERNAME_FIELD='username'
    
    REQUIRED_FIELDS=['email']
   
    objects=UserManager()
    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return True
        
    def has_module_perms(self,app_label):
        return True
# fekkonam in vase ineke too panele admin beshe estefade kard.
    @property
    def is_staff(self):
        return self.is_admin
from django.utils import timezone

class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phonenumber=models.IntegerField(blank=True,null=True)
    userplan=models.CharField(blank=True,max_length=255)
    paiduntil = models.DateField(null=True, blank=True)
     
 
    def __str__(self):
        return self.user.username 

    def setpaiduntil(self,dateortimestamp):
        if isinstance(dateortimestamp,int):
            paiduntil=datetime.date.fromtimestamp(dateortimestamp)
        elif isinstance(dateortimestamp,str):
            paiduntil=datetime.date.fromtimestamp(int(dateortimestamp))
        else:
            paiduntil=dateortimestamp
        self.paiduntil=paiduntil
        self.save()

    def haspaid(self, currentdate=datetime.date.today()):
        if self.paiduntil is None:
            return False
        return currentdate < self.paiduntil






def saveprofileuser(sender,**kwargs):
    if kwargs['created']: 
        Userprofile.objects.create(user=kwargs['instance'])

post_save.connect(saveprofileuser,sender=User)