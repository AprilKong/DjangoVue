from rest_framework import mixins
from rest_framework import generics
import sys
sys.path.append("..")
from iiot_api import models
from iiot_api import serializers
class DeviceList(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class PoolList(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = models.SteamPool.objects.all()
    serializer_class = serializers.PoolSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class PoolInfo(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = models.PoolInfo.objects.raw('SELECT * FROM iiot_api_poolinfo WHERE id IN (SELECT max( id ) FROM iiot_api_poolinfo GROUP BY steampool_id )')
    serializer_class = serializers.PoolInfoSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
