Django Binance WebSocket API
### Этот проект представляет собой Django-приложение с интеграцией WebSocket для получения данных из публичного API Binance. WebSocket-соединение используется для получения информации о рыночных ценах в реальном времени.

## 🚀 Функционал

- Подключение к WebSocket Binance.

- Обработка и сохранение данных о ценах в PostgreSQL.

- Автоматическое переподключение при разрыве соединения.

- Django Channels для обработки WebSocket-сообщений.
---
## 🛠 Установка и запуск

1. Клонирование репозитория
```
git clone https://github.com/gigabait15/BinanseAPI.git
cd BinanceAPI
```
2. Создание виртуального окружения
``` 
python -m venv .venv
source .venv/bin/activate  # Для Linux/macOS
.venv\Scripts\activate  # Для Windows
```
3.  Установка зависимостей
``` 
pip install -r requirements.txt
```
4. Настройка базы данных (PostgreSQL)

Убедитесь, что у вас установлена PostgreSQL. Запустить скрипт и добавить настройки или создать файл .env вручную и заполнить поля для БД:
```bash
touch .env
{
  echo "NAME="
  echo "USER="
  echo "PASSWORD="
  echo "HOST="
  echo "PORT="
} >> .env
echo ".env файл создан или обновлен."
 ```
5. Применение миграций
``` 
python manage.py migrate
```
6. Запуск сервера
```
python manage.py runserver
```
7. Запуск WebSocket-клиента
```
python .\chats\ws.py
```
8. Запуск подключения к клиенту
```
python .\chats\client.py
```
---
## 📂 Структура проекта
``` 
BinanceAPI/
├── chats/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── client.py
│   ├── consumers.py
│   ├── models.py
│   ├── routing.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── ws.py
│
├── config/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── __init__.py
│
├── .gitignore
├── README.md
├── manage.py
├── requirements.txt
```