from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkoutadr/<int:item_id>/', views.checkoutadr, name='checkoutadr'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
    path('wh/', webhook, name='webhook'),
    path('cache_checkout_data/',
         views.cache_checkout_data, name='cache_checkout_data'),
]
