from django.urls import path
from wishlist.views import show_wishlist

from wishlist.views import request_xml #Import fungsi yang sudah dibuat di wishlist\view
from wishlist.views import request_json #Import fungsi yang sudah dibuat di wishlist\view

from wishlist.views import show_json_by_id #Import fungsi yang sudah dibuat di wishlist\view

from wishlist.views import register # Import fungsi register untuk form registrasi (Lab 3)
from wishlist.views import login_user # Import fungsi Login (Lab 3)
from wishlist.views import logout_user # Import fungsi logout (Lab 3)

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', request_xml, name='request_xml'),
    path('json/', request_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), #sesuaikan dengan nama fungsi yang dibuat
    path('register/', register, name='register'), #lab 3 (form register)
    path('login/', login_user, name='login'), # Lab 3 (Handle Login)
    path('logout/', logout_user, name='logout'), # Lab 3 (Handle Logout)
]