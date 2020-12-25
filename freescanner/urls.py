from django.urls import path
from . import views

urlpatterns = [
    path('', views.free_scanner, name='freescanner'),
    path('identifiers/', views.identifiers, name='identifiers'),
]
