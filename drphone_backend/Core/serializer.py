from rest_framework import serializers
from .models import Phones, PhonesOptions, Accessories, Covers, IMac, IMacOptions, AccessoriesOptions
from BaseSettings.serializer import ColorProductSerializer, MemoryProductsSerializer, SIMProductSerializer, ManufacturerSerializer, ImagesProductSerializer


class PhonesSerializer(serializers.ModelSerializer):
    allColors = ColorProductSerializer(many=True)
    allMemory = MemoryProductsSerializer(many=True)
    allSim = SIMProductSerializer(many=True)
    manufacturer = ManufacturerSerializer(read_only=True)
    class Meta:
        model = Phones
        fields = '__all__'


class PhoneUtilSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = ['name']


class PhonesOptionsSerializer(serializers.ModelSerializer):
    phone = PhonesSerializer(read_only=True)
    color = ColorProductSerializer(read_only=True)
    memory = MemoryProductsSerializer(read_only=True)
    sim = SIMProductSerializer(read_only=True)
    images = ImagesProductSerializer(many=True)
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
