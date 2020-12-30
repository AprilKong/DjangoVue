from rest_framework import mixins
from rest_framework import generics
import sys
sys.path.append("..")
from models import Device
from serializers import DeviceSerializer
class DeviceList(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
