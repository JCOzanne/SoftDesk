from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user.views import UserViewSet

user_router = routers.SimpleRouter()
user_router.register('User', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(user_router.urls))
]
