from django.http.response import JsonResponse
from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import *
from rest_framework_simplejwt.tokens import  AccessToken

 
    
class Userserializer(serializers.ModelSerializer):
    # id=serializers.SerializerMethodField(read_only=True)
    # username=serializers.SerializerMethodField(read_only=True)
    isadmin=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields=['id','username','email','isadmin']
        # fields='__all__'

    # def get_username(self,obj):
    #     username=obj.username
    #     if username=='':
    #         username=obj.email
    #     return username

    def get_isadmin(self,obj):
        isadmin=obj.is_admin
        return isadmin

    # def get_id(self,obj):
    #     return obj.id

class Userserializerwithtoken(Userserializer):
    token=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields=['id','username','email','isadmin','token']
    def get_token(self,obj):
        # token=RefreshToken.for_user(obj)
        token=AccessToken.for_user(obj)
        return str(token)

class Userprofileserializerwithtoken(serializers.ModelSerializer):
    token=serializers.SerializerMethodField(read_only=True)
    username=serializers.SerializerMethodField(read_only=True)
    email=serializers.SerializerMethodField(read_only=True)
    isadmin=serializers.SerializerMethodField(read_only=True)
    haspaid=serializers.SerializerMethodField(read_only=True)
    userplan=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Userprofile
        fields=['id','username','email','phonenumber','isadmin','token','userplan','paiduntil','haspaid']

    def get_token(self,obj):
        token=AccessToken.for_user(obj.user)
        return str(token)
    def get_username(self,obj):
        return obj.user.username
    def get_userplan(self,obj):
        return obj.userplan.split(' ')
    def get_email(self,obj):
        return obj.user.email
    def get_isadmin(self,obj):
        return obj.user.is_admin
    def get_haspaid(self,obj):
        return obj.haspaid()