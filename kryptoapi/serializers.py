from rest_framework import serializers
from .models import *

class ALertSerializer(serializers.ModelSerializer):
    class Meta:
        model = alert
        fields = ['id','name','threshold','description','status']
        read_only = ['status']

class CreateALertSerializer(serializers.ModelSerializer):
    class Meta:
        model = alert
        fields = ['id','name','threshold','description']
        read_only = ['status']

class ALertUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = alert
        #exclude = ('id','name','threshold','description','author','status')
        fields = ['id']
