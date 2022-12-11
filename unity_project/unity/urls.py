from django.urls import include, path

from . import views

urlpatterns = [
    path("store_email", views.CreateEmailView.as_view()),
]
