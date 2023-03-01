from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view),
    path('district/<int:district_id>/', views.district_detail_view),
    path('new_request', views.new_request),
]