from django.urls import path
from . import views


urlpatterns = [
    path('', views.wallet_scanner, name='walletscanner'),
    path('mainwallet/', views.mwallet, name='mwallet'),
]
