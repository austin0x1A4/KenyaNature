from django.urls import path
from . import views
app_name = 'homepage'

urlpatterns = [
    path("", views.index, name="index"),
    path("nature", views.nature, name="nature"),
    path("energy", views.energy, name="energy"),
    path("about", views.about, name="about"),
    path('privacy', views.privacy, name="privacy"),
    path('contact', views.contact, name="contact")
]