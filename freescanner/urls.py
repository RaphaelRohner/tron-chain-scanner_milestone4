from django.urls import path
from . import views

urlpatterns = [
    path('', views.freescanner, name='freescanner'),
    path('add/', views.identifiers, name='identifiers'),
    path('edit/<int:item_id>/', views.edit_contracts, name='edit_contracts'),  # noqa: E501
]
