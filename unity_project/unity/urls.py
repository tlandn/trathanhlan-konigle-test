from django.urls import path, include
from . import views

urlpatterns = [
    path('store_email', views.CreateEmailView.as_view()),
]
