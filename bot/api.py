import asyncio
import hmac
import hashlib
import json
import requests
from fastapi import FastAPI, Request, HTTPException, Header
from pydantic import BaseModel

app = FastAPI(title='NartRental Bot API')

# Конфигурация
NOTIFY_SECRET = 'dev-secret-change-in-production'
BOT_API_URL = 'http://localhost:8002'  # URL для связи с ботом

print(f'🚀 Запуск FastAPI сервера...')
print(f'🔑 NOTIFY_SECRET: {NOTIFY_SECRET[:10]}...')
print(f'🤖 BOT_API_URL: {BOT_API_URL}')


class OrderNotification(BaseModel):
    order_id: int
    product: str
    price: int
    customer_name: str
    customer_phone: str
    comment: str
    created_at: str
    section: str | None = None


@app.get('/ping')
async def ping():
    return {
        'message': 'pong',
        'service': 'FastAPI',
        'bot_url': BOT_API_URL
    }


@app.post('/notify/new-order')
async def notify_new_order(
    order: OrderNotification,
    request: Request,
    x_signature: str = Header(None)
):
    if not x_signature:
        raise HTTPException(status_code=400, detail='Missing signature')

    body = await request.body()
    expected_signature = hmac.new(
        NOTIFY_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(x_signature, expected_signature):
        raise HTTPException(status_code=401, detail='Invalid signature')

    # Формируем сообщение для бота
    message_text = f'''🆕 Новый заказ #{order.order_id}
Товар: {order.product}
Раздел: {order.section or 'не указан'}
Цена: {order.price // 100} ₽
Имя: {order.customer_name}
Телефон: {order.customer_phone}'''

    if order.comment:
        message_text += f'\nКомментарий: {order.comment}'

    # Отправляем уведомление через HTTP API бота
    try:
        response = requests.post(
            f'{BOT_API_URL}/send-notification',
            json={'message': message_text},
            timeout=5
        )

        if response.status_code == 200:
            result = response.json()
            print(f'✅ Уведомление отправлено: {result}')
            return {'message': 'Notification sent successfully'}
        else:
            print(f'❌ Ошибка отправки: {response.status_code}')
            return {'message': 'Failed to send notification'}

    except Exception as e:
        print(f'❌ Ошибка связи с ботом: {e}')
        return {'message': 'Bot communication error'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8001)
