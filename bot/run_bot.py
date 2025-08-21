import subprocess
import time
import sys
import os


def run_bot():
    """Запуск Telegram бота"""
    print('🤖 Запуск Telegram бота...')
    try:
        subprocess.run([sys.executable, 'bot.py'], check=True)
    except KeyboardInterrupt:
        print('🛑 Бот остановлен')
    except Exception as e:
        print(f'❌ Ошибка запуска бота: {e}')


def run_bot_api():
    """Запуск HTTP API бота"""
    print('🌐 Запуск Bot HTTP API...')
    try:
        subprocess.run([sys.executable, 'bot_api.py'], check=True)
    except KeyboardInterrupt:
        print('🛑 Bot API остановлен')
    except Exception as e:
        print(f'❌ Ошибка запуска Bot API: {e}')


def run_fastapi():
    """Запуск FastAPI сервера"""
    print('🚀 Запуск FastAPI сервера...')
    try:
        subprocess.run([sys.executable, 'api.py'], check=True)
    except KeyboardInterrupt:
        print('🛑 FastAPI остановлен')
    except Exception as e:
        print(f'❌ Ошибка запуска FastAPI: {e}')


if __name__ == '__main__':
    print('🚀 Запуск всех сервисов бота...')

    # Запускаем все сервисы в отдельных процессах
    processes = []

    try:
        # Запуск бота
        bot_process = subprocess.Popen([sys.executable, 'bot.py'])
        processes.append(bot_process)
        print('✅ Telegram бот запущен')

        time.sleep(2)

        # Запуск Bot HTTP API
        bot_api_process = subprocess.Popen([sys.executable, 'bot_api.py'])
        processes.append(bot_api_process)
        print('✅ Bot HTTP API запущен')

        time.sleep(2)

        # Запуск FastAPI
        fastapi_process = subprocess.Popen([sys.executable, 'api.py'])
        processes.append(fastapi_process)
        print('✅ FastAPI сервер запущен')

        print('\n🎉 Все сервисы запущены!')
        print('🤖 Telegram бот: работает')
        print('🌐 Bot HTTP API: http://localhost:8002')
        print('🚀 FastAPI: http://localhost:8001')
        print('\n💡 Отправьте /admin боту для регистрации')
        print('⏹️  Нажмите Ctrl+C для остановки')

        # Ждем завершения всех процессов
        for process in processes:
            process.wait()

    except KeyboardInterrupt:
        print('\n🛑 Остановка всех сервисов...')
        for process in processes:
            process.terminate()
        print('✅ Все сервисы остановлены')
    except Exception as e:
        print(f'❌ Ошибка: {e}')
        for process in processes:
            process.terminate()
