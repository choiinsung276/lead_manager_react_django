from django.urls import path, include
from .api import RegisterAPI, LoginAPI
from knox import views as knox_views

urlpatterns =[
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()), # 제네릭 뷰라서 as_view
    path('api/auth/login', LoginAPI.as_view())
]