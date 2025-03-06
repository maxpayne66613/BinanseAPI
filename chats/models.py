from django.db import models


class CryptoPrice(models.Model):
    """
    Модель для хранения информации о цене криптовалюты.

    Атрибуты:
    - symbol (str): Тикер криптовалютной пары (например, BTCUSDT).
    - price (Decimal): Цена актива с точностью до 8 знаков.
    - timestamp (datetime): Время сохранения записи (автоматически заполняется).
    """

    symbol: str = models.CharField(max_length=10, db_index=True, verbose_name="Тикер")
    price: float = models.DecimalField(max_digits=20, decimal_places=8, verbose_name="Цена")
    timestamp: str = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Время записи")

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = "Цена криптовалюты"
        verbose_name_plural = "Цены криптовалют"

    def __str__(self) -> str:
        """Строковое представление объекта."""
        return f"{self.symbol}: {self.price}"
