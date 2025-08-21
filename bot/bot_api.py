import asyncio
import json
from fastapi import FastAPI, Request
from pydantic import BaseModel
from bot import bot, get_admin_ids, send_notification

app = FastAPI(title='Bot HTTP API')


class NotificationRequest(BaseModel):
    message: str


@app.get('/ping')
async def ping():
    return {
        'message': 'pong',
        'service': 'Bot HTTP API',
        'admin_count': len(get_admin_ids())
    }


@app.post('/send-notification')
async def send_notification_endpoint(request: NotificationRequest):
    admin_ids = get_admin_ids()

    if not admin_ids:
        return {'message': 'No admin IDs configured', 'sent': 0}

    success_count = 0
    for admin_id in admin_ids:
        try:
            await send_notification(admin_id, request.message)
            success_count += 1
        except Exception as e:
            print(f'❌ Ошибка отправки {admin_id}: {e}')

    return {
        'message': f'Notification sent to {success_count}/{len(admin_ids)} admins',
        'sent': success_count,
        'total': len(admin_ids)
    }


@app.get('/admin-ids')
async def get_admin_ids_endpoint():
    return {
        'admin_ids': get_admin_ids(),
        'count': len(get_admin_ids())
    }

if __name__ == '__main__':
    import uvicorn
    print('🤖 Запуск Bot HTTP API...')
    uvicorn.run(app, host='0.0.0.0', port=8002)
