import asyncio
import websockets
import json


async def connect() -> None:
    """
    Подключается к WebSocket-серверу на localhost:8000/ws/binance/,
    получает данные о криптовалюте и выводит их в консоль.
    """
    async with websockets.connect("ws://localhost:8000/ws/binance/") as websocket:
        print("Подключено к WebSocket")
        try:
            while True:
                # Получаем сообщение от сервера
                message: str = await websocket.recv()
                data: dict = json.loads(message)

                symbol: str = data.get("symbol", "Unknown")
                price: str = data.get("price", "N/A")

                print(f"{symbol} - {price}")
        except websockets.ConnectionClosed:
            print("Соединение закрыто")


if __name__ == "__main__":
    asyncio.run(connect())
