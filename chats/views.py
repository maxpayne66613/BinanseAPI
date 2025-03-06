from rest_framework import generics, filters
from .models import CryptoPrice
from .serializers import CryptoPriceSerializer


class CryptoPriceListView(generics.ListAPIView):
    """
    API для получения списка цен криптовалют.

    - Отображает данные в порядке убывания по `timestamp`.
    - Поддерживает фильтрацию по `symbol`.
    - Поддерживает пагинацию.
    """

    queryset = CryptoPrice.objects.all().order_by("-timestamp")
    serializer_class = CryptoPriceSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ["symbol"]
