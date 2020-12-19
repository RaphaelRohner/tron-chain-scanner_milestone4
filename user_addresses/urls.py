from django.urls import path
from . import views

urlpatterns = [
    path('', views.address, name='addresses'),
    path('<item_id>/', views.address, name='addresses'),
    path('edit/<int:item_id>/', views.edit_address, name='edit_address'),
    path('delete/<int:item_id>/', views.delete_address, name='delete_address'),
]
