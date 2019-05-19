from django.urls import path
from . import views

# The paths tell what view to use

urlpatterns = [
    path('', views.home, name='project-home'),
    path('DDOSExplained/', views.DDOSExplained, name='project-Josh'),
    path('DDOSHistory/', views.DDOSHistory, name='project-Andrew'),
    path('DDOSProtection/', views.DDOSProtection, name='project-Cheif'),
]