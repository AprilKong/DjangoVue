from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'add_book$', add_book, ),
    # url(r'show_books$', show_books, ),
    url(r'get_devicess$', views.DeviceList.as_view(), ),
]
