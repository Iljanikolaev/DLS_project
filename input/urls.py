from django.urls import path, include
from .views import *

urlpatterns =  [#path('login/', user_login, name = 'login'),
				#path('logout/', user_logout, name = 'logout'),
				path('input/', load_images, name = 'input'),
				]