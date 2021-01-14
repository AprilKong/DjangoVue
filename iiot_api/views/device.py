from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
import datetime
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

class AllPoolInfo(mixins.ListModelMixin,generics.GenericAPIView):
    #queryset = models.PoolInfo.objects.order_by('collect_time')[0]
    serializer_class = serializers.PoolInfoSerializer
    #filter_backends = (filters.SearchFilter, )
    #search_fields = ('=steampool_id__id',)
    query = 'select * from iiot_site_db.iiot_api_poolinfo a join iiot_site_db.iiot_api_steampool b on a.steampool_id = b.id where a.id in (select max(id) from iiot_site_db.iiot_api_poolinfo group by steampool_id) and b.device_id = 1' % lname
    def get_object(self):
        keyword = self.request.query_params.get('device')
        if not keyword:
            queryset = 'select * from iiot_site_db.iiot_api_poolinfo a join iiot_site_db.iiot_api_steampool b on a.steampool_id = b.id where a.id in (select max(id) from iiot_site_db.iiot_api_poolinfo group by steampool_id) and b.device_id = %d' % 1
        else:
            queryset = 'select * from iiot_site_db.iiot_api_poolinfo a join iiot_site_db.iiot_api_steampool b on a.steampool_id = b.id where a.id in (select max(id) from iiot_site_db.iiot_api_poolinfo group by steampool_id) and b.device_id = %d' % keyword
        return queryset
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class PoolInfoHistory(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = models.PoolInfo.objects.all()
    serializer_class = serializers.PoolInfoSerializer

    def get_object(self):
        offset = self.request.query_params.get('q')
        pool = self.request.query_params.get('p')
        #当前日期格式
        cur_date = datetime.datetime.now().date()
        #前一天日期
        yester_day = cur_date - datetime.timedelta(days=1)

        offset_day = cur_date - datetime.timedelta(days=offset)

        if not offset:
            queryset = models.SystemInfo.objects.filter(steampool_id__id=pool).filter(collect_time__gt=yester_day,collect_time__lte=cur_date)
        else:
            queryset = models.SystemInfo.objects.filter(steampool_id__id=pool).filter(collect_time__gte=offset_day,collect_time__lte=cur_date)
        return queryset

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

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

class SystemInfoHistory(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = models.SystemInfo.objects.all()
    serializer_class = serializers.SystemInfoSerializer

    def get_object(self):
        offset = self.request.query_params.get('q')
        device = self.request.query_params.get('d')
        #当前日期格式
        cur_date = datetime.datetime.now().date()
        #前一天日期
        yester_day = cur_date - datetime.timedelta(days=1)

        offset_day = cur_date - datetime.timedelta(days=offset)

        if not offset:
            queryset = models.SystemInfo.objects.filter(device_id__id=device).filter(collect_time__gt=yester_day,collect_time__lte=cur_date)
        else:
            queryset = models.SystemInfo.objects.filter(device_id__id=device).filter(collect_time__gte=offset_day,collect_time__lte=cur_date)
        return queryset

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
