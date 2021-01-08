from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
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

class PoolInfo(mixins.RetrieveModelMixin,generics.GenericAPIView):
    #queryset = models.PoolInfo.objects.order_by('collect_time')[0]
    serializer_class = serializers.PoolInfoSerializer
    #filter_backends = (filters.SearchFilter, )
    #search_fields = ('=steampool_id__id',)
    def get_object(self):
        keyword = self.request.query_params.get('q')
        if not keyword:
            queryset = models.PoolInfo.objects.order_by('collect_time')[0]
        else:
            queryset = models.PoolInfo.objects.all().filter(steampool_id__id=keyword).order_by('collect_time')[0]
        return queryset
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class SystemInfo(mixins.RetrieveModelMixin,generics.GenericAPIView):
    #queryset = models.PoolInfo.objects.order_by('collect_time')[0]
    serializer_class = serializers.SystemInfoSerializer
    #filter_backends = (filters.SearchFilter, )
    #search_fields = ('=steampool_id__id',)
    def get_object(self):
        keyword = self.request.query_params.get('q')
        if not keyword:
            queryset = models.SystemInfo.objects.order_by('collect_time')[0]
        else:
            queryset = models.SystemInfo.objects.all().filter(device_id__id=keyword).order_by('collect_time')[0]
        return queryset
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
