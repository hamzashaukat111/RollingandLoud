from django.urls import path
from . import views  # Import your website views here

urlpatterns = [
    path("", views.home, name="home"),
    # Define more URL patterns as needed
]
