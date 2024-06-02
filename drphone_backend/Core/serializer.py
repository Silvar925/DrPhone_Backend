from rest_framework import serializers
from .models import Phones, PhonesOptions, Accessories, Covers, IMac, IMacOptions, AccessoriesOptions


class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = '__all__'


class PhonesOptionsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PhonesOptions
        fields = '__all__'
        

class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = '__all__'


class AccessoriesOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoriesOptions
        fields = '__all__'


class CoversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covers
        fields = '__all__'


class IMacSerializer(serializers.ModelSerializer):
    class Meta: 
        model = IMac
        fields = '__all__'


class IMacOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IMacOptions
        fields = '__all__'