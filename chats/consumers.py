import json
import asyncio
import websockets
from channels.generic.websocket import AsyncWebsocketConsumer


BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@ticker"


class BinanceConsumer(AsyncWebsocketConsumer):
    """
    WebSocket-консьюмер для получения данных с Binance и отправки их клиенту.

    - Подключается к Binance WebSocket API.
    - Получает информацию о цене BTC/USDT.
    - Каждую минуту отправляет обновленные данные подключенным клиентам.
    """

    async def connect(self) -> None:
        """При подключении клиента создаёт WebSocket-поток для получения данных."""
        await self.accept()
        self.binance_task = asyncio.create_task(self.binance_stream())

    async def disconnect(self, close_code: int) -> None:
        """Останавливает WebSocket-поток при отключении клиента."""
        if hasattr(self, "binance_task"):
            self.binance_task.cancel()

    async def binance_stream(self) -> None:
        """
        Подключается к Binance WebSocket API и получает обновления о цене BTC/USDT.
        Отправляет данные клиенту каждые 60 секунд.
        """
        async with websockets.connect(BINANCE_WS_URL) as websocket:
            while True:
                data: str = await websocket.recv()
                parsed_data: dict = json.loads(data)

                symbol: str = parsed_data.get("s", "Unknown")
                price: str = parsed_data.get("c", "N/A")

                # Отправка данных клиенту
                await self.send(json.dumps({"symbol": symbol, "price": price}))

                await asyncio.sleep(60)
