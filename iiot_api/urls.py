from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'add_book$', add_book, ),
    # url(r'show_books$', show_books, ),
    url(r'get_devices$', views.DeviceList.as_view()),
    url(r'get_pools$', views.PoolList.as_view()),
    url(r'get_poolinfo$', views.PoolInfo.as_view(),base_name="id")
]
