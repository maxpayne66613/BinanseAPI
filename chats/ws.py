import asyncio
import sys
import os
import json
import logging
import websockets
from django.utils.timezone import now
from asgiref.sync import sync_to_async

import django

# Настройка Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from chats.models import CryptoPrice

# Константы
BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@ticker"
# Время задержки перед повторным подключением (сек)
RECONNECT_DELAY = 5
# Интервал между обработкой данных (сек)
RECEIVE_INTERVAL = 60

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@sync_to_async
def save_to_db(symbol: str, price: float) -> None:
    """Сохранение данных в базу."""
    CryptoPrice.objects.create(symbol=symbol, price=price, timestamp=now())
    logger.info(f"Сохранено в БД: {symbol} - {price}")


async def binance_ws() -> None:
    """Подключение к WebSocket Binance и получение данных."""
    while True:
        try:
            async with websockets.connect(BINANCE_WS_URL) as websocket:
                logger.info("Подключено к Binance WebSocket")
                while True:
                    data = await websocket.recv()
                    parsed_data = json.loads(data)

                    symbol = parsed_data.get("s", "UNKNOWN")
                    price = float(parsed_data.get("c", 0))

                    await save_to_db(symbol, price)
                    await asyncio.sleep(RECEIVE_INTERVAL)

        except (websockets.ConnectionClosed, asyncio.TimeoutError) as e:
            logger.warning(f"Соединение потеряно: {e}. Переподключение через {RECONNECT_DELAY} сек...")
            await asyncio.sleep(RECONNECT_DELAY)


if __name__ == "__main__":
    asyncio.run(binance_ws())
