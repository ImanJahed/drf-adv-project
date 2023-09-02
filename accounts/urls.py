from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserApiView
urlpatterns = [
    path('', UserApiView.as_view()),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),


]