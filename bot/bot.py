import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Конфигурация бота
BOT_TOKEN = '8466417948:AAHIx_W3tQ8z8__zzwg82tjh0sgALlqQW5Y'
ADMIN_IDS = [123456789]  # Начальный список админов

print(f'🤖 Запуск Telegram бота...')
print(f'✅ BOT_TOKEN: {BOT_TOKEN[:10]}...')
print(f'👥 ADMIN_IDS: {ADMIN_IDS}')

# Создаем бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Регистрируем команду /admin


@dp.message(Command("admin"))
async def admin_command(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name

    print(f'📨 Получена команда /admin от {user_id} ({username})')

    # Добавляем в список администраторов
    if user_id not in ADMIN_IDS:
        ADMIN_IDS.append(user_id)
        print(f'✅ Новый админ добавлен: {user_id} ({username})')
        await message.reply(
            f'🎉 Поздравляем! Вы успешно зарегистрированы как администратор.\n'
            f'🆔 Ваш ID: {user_id}\n'
            f'👤 Username: @{username}\n\n'
            f'📝 Теперь вы будете получать уведомления о новых заказах!'
        )
    else:
        await message.reply(
            f'👋 Вы уже являетесь администратором!\n'
            f'🆔 Ваш ID: {user_id}\n'
            f'👤 Username: @{username}'
        )

# Функция для отправки уведомлений


async def send_notification(admin_id: int, message_text: str):
    try:
        await bot.send_message(admin_id, message_text)
        print(f'✅ Уведомление отправлено админу {admin_id}')
        return True
    except Exception as e:
        print(f'❌ Ошибка отправки сообщения {admin_id}: {e}')
        return False

# Функция для получения списка админов


def get_admin_ids():
    return ADMIN_IDS.copy()


print('✅ Команда /admin зарегистрирована')
print('🔄 Запуск polling...')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
