"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView

from cars.views import *
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')), #Подключена авторизация на основе сессий
    path('api/v1/cars/', CarsAPIList.as_view()),
    path('api/v1/cars/<int:pk>/', CarsAPIUpdate.as_view()),
    path('api/v1/carsdelete/<int:pk>/', CarsAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]








# router = routers.DefaultRouter()
# router.register(r'cars', CarsViewSet)
# print(router.urls)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include(router.urls)), #http://127.0.0.1:8000/api/v1/cars/
#     # path('api/v1/carslist/', CarsViewSet.as_view({'get': 'list'})),
#     # path('api/v1/carslist/<int:pk>/', CarsViewSet.as_view({'put': 'update'})),
# ]
