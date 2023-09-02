from django.urls import path

from . import views

urlpatterns = [
    path("list", views.AdApiView.as_view()),
    path('add', views.AdCreateApiView.as_view()),
    path('detail/<int:pk>', views.AdDetailApiView.as_view()),
    path('search/', views.AdSearchApiView.as_view()),
    ]
