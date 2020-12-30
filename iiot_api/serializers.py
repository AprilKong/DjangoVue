from rest_framework import serializers
from .models import Device,SteamPool,PoolInfo

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteamPool
        fields = '__all__'

class PoolInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolInfo
        fields = '__all__'
