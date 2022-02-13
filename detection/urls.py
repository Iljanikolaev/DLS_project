from django.urls import path, include
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns =  [#path('login/', user_login, name = 'login'),
                #path('logout/', user_logout, name = 'logout'),
                path('detection/<int:pk>', detection_obj, name = 'detection'),
                ]