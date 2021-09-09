from django.urls import path, include
from .api import RegisterAPI
from knox import views as knox_views

urlpatterns =[
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()) # 제네릭 뷰라서 as_view
]