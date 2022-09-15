from django.urls import path
from wishlist.views import show_wishlist

from wishlist.views import request_xml #Import fungsi yang sudah dibuat di wishlist\view
from wishlist.views import request_json #Import fungsi yang sudah dibuat di wishlist\view

from wishlist.views import show_json_by_id #Import fungsi yang sudah dibuat di wishlist\view

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', request_xml, name='request_xml'),
    path('json/', request_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), #sesuaikan dengan nama fungsi yang dibuat
]