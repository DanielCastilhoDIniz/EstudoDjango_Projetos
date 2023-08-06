from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('recipes/<i    nt:id>/', views.recipe),
]
