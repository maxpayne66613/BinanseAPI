from rest_framework import serializers
from .models import CryptoPrice


class CryptoPriceSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели CryptoPrice.

    Преобразует данные о ценах криптовалют в JSON и обратно.
    """

    formatted_price = serializers.SerializerMethodField()

    class Meta:
        model = CryptoPrice
        fields = "__all__"
        read_only_fields = ("timestamp",)

    def get_formatted_price(self, obj: CryptoPrice) -> str:
        """Возвращает цену в отформатированном виде."""
        return f"{obj.price:.8f}"
