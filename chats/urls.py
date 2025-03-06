from django.urls import path
from .views import CryptoPriceListView

urlpatterns = [
    path('prices/', CryptoPriceListView.as_view(), name='crypto-prices'),
]