#!/bin/bash

echo "🚀 Запуск NartRental..."

if [ ! -f .env ]; then
    echo "📝 Создание .env файла..."
    cp env.sample .env
    echo "⚠️  Отредактируйте .env файл с реальными значениями!"
fi

echo "🐳 Запуск Docker Compose..."
make up

echo "⏳ Ожидание запуска сервисов..."
sleep 15

echo "🗄️  Применение миграций..."
make migrate

echo "🌱 Создание демо-данных..."
make seed

echo "✅ Готово!"
echo "🌐 Главная: http://localhost"
echo "📦 Товары: http://localhost/products"
echo "🔧 API: http://localhost/api/"
echo "📊 Админка: http://localhost/admin"
echo "🤖 Bot API: http://localhost/notify/"
echo ""
echo "💡 Все сервисы доступны через единый порт 80!"
echo ""
echo "📋 Для просмотра логов: make logs"
echo "📋 Для остановки: make down" 