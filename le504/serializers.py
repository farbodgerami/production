 
from rest_framework import serializers
 
from .models import *
 

# class Levelserializer(serializers.ModelSerializer):
#     id=serializers.SerializerMethodField(read_only=True)
#     user=serializers.SerializerMethodField(read_only=True)
#     kalame=serializers.SerializerMethodField(read_only=True)
#     mani=serializers.SerializerMethodField(read_only=True)
#     lesson=serializers.SerializerMethodField(read_only=True)
#     description=serializers.SerializerMethodField(read_only=True)
#     audiofile=serializers.SerializerMethodField(read_only=True)

     
#     class Meta:
#         model=Level      
#         fields=['id','level',
#         'kalame',
#         'mani',
#         'description','lesson',
#         'user','audiofile']
    
#     def get_kalame(self,obj):
#         return obj.word.kalame
#     def get_mani(self,obj):
#         return obj.word.maani
#     def get_description(self,obj):
#         return obj.word.description
#     def get_lesson(self,obj):
#         return obj.word.lesson
#     def get_audiofile(self,obj):
#         return f'/media/{obj.word.audiofile}'   
#     def get_user(self,obj):
#         return obj.user.username
#     def get_id(self,obj):
#         return obj.id
  
class wordsserializer(serializers.ModelSerializer):
    class Meta:
        model=Word
        fields='__all__'
     