from rest_framework import serializers
from .models import ColorProduct, ImagesProduct, NewDevices, UsedDevices, Accessories, Covers, IMac


class NewDevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewDevices
        fields = "__all__"


class UsedDevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsedDevices
        fields = "__all__"


class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = "__all__"


class CoversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covers
        fields = "__all__"


class IMacSerializer(serializers.ModelSeriazalizer):
    class Meta:
        model = IMac
        fields = "__all__"


class ColorProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorProduct
        fields = "__all__"


class ImagesProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesProduct
        fields = "__all__"