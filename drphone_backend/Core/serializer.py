from rest_framework import serializers
from .models import Phones, PhonesOptions, Accessories, Covers, IMac, IMacOptions, AccessoriesOptions, CoversOptions
from BaseSettings.serializer import ColorProductSerializer, MemoryProductsSerializer, SIMProductSerializer, \
    ManufacturerSerializer, ImagesProductSerializer


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
    device = PhonesSerializer(read_only=True)
    color = ColorProductSerializer(read_only=True)
    memory = MemoryProductsSerializer(read_only=True)
    sim = SIMProductSerializer(read_only=True)
    images = ImagesProductSerializer(many=True)

    class Meta:
        model = PhonesOptions
        fields = '__all__'


class PhoneOptionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhonesOptions
        fields = ['unique_id']


class AccessoriesSerializer(serializers.ModelSerializer):
    allColors = ColorProductSerializer(many=True)
    
    class Meta:
        model = Accessories
        fields = '__all__'


class AccessoriesOptionsSerializer(serializers.ModelSerializer):
    device = AccessoriesSerializer(read_only=True)
    color = ColorProductSerializer(read_only=True)
    memory = MemoryProductsSerializer(read_only=True)
    images = ImagesProductSerializer(many = True, read_only=True)

    class Meta:
        model = AccessoriesOptions
        fields = '__all__'


class CoversSerializer(serializers.ModelSerializer):
    allColors = ColorProductSerializer(many=True)

    class Meta:
        model = Covers
        fields = '__all__'


class CoversOptionsSerializer(serializers.ModelSerializer):
    device = CoversSerializer(read_only=True)
    color = ColorProductSerializer(read_only=True)
    images = ImagesProductSerializer(many = True, read_only=True)

    class Meta:
        model = CoversOptions
        fields = '__all__'


class IMacSerializer(serializers.ModelSerializer):
    allColors = ColorProductSerializer(many=True)
    allMemory = MemoryProductsSerializer(many=True)

    class Meta:
        model = IMac
        fields = '__all__'


class IMacOptionsSerializer(serializers.ModelSerializer):
    device = IMacSerializer(read_only=True)
    color = ColorProductSerializer(read_only=True)
    memory = MemoryProductsSerializer(read_only=True)
    images = ImagesProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = IMacOptions
        fields = '__all__'