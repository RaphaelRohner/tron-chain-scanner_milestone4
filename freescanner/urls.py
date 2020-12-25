from django.urls import path
from . import views

urlpatterns = [
    path('', views.freescanner, name='freescanner'),
    path('add/', views.identifiers, name='identifiers'),
    path('edit/<int:item_id>/', views.edit_identifier, name='edit_identifier'),  # noqa: E501
    path('delete/<int:item_id>/', views.delete_identifier, name='delete_identifier'),  # noqa: E501
]
