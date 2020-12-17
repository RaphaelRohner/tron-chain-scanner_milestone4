from django.urls import path
from . import views

urlpatterns = [
    path('', views.address, name='addresses'),
    path('<item_id>/', views.address, name='addresses')
]
