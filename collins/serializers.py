 
from rest_framework import serializers
 
from .models import *
 
 
class wordsserializer(serializers.ModelSerializer):
    class Meta:
        model=Word
        fields='__all__'
     