from django.conf.urls import url, include
from . import views

#from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'get_poolinfo',views.PoolInfo,'id')

urlpatterns = [
    # url(r'add_book$', add_book, ),
    # url(r'show_books$', show_books, ),
    url(r'get_devices$', views.DeviceList.as_view()),
    url(r'get_pools$', views.PoolList.as_view()),
    url(r'get_poolinfo$', views.PoolInfo.as_view(),name='id'),
]
