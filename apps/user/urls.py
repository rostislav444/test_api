from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

app_name = 'user'

router = routers.SimpleRouter()

router.register('register', views.RegisterView, basename='register')
router.register('', views.UserView, basename='profile')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
] + router.urls
