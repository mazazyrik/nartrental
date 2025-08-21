# NartRental - Аренда оборудования

Монорепозиторий для системы аренды оборудования с веб-интерфейсом и Telegram-уведомлениями.

## 🎯 Особенности

- **Логотип**: Использует фирменный логотип NartRental с историческими мотивами
- **Дизайн**: Пиксель-перфект относительно макета с адаптивностью
- **UX**: Современный интерфейс с плавными анимациями и hover-эффектами
- **Безопасность**: HMAC-подпись для уведомлений в Telegram
- **Nginx**: Единый прокси-сервер на порту 80 для всех сервисов

## 🏗️ Структура

- `frontend/` - Next.js 14 + TypeScript + TailwindCSS
- `backend/` - Django 5 + DRF + PostgreSQL
- `bot/` - Telegram бот на aiogram 3 + FastAPI
- `deploy/` - Docker Compose + Nginx конфигурация
- `maket/` - Макеты дизайна

## 🚀 Быстрый старт

### 1. Подготовка
```bash
# Клонируйте репозиторий
git clone <your-repo>
cd nartrental

# Скопируйте переменные окружения
cp env.sample .env
```

### 2. Настройка .env
Отредактируйте `.env` файл:
```bash
# Заполните реальные значения
BOT_TOKEN=your-telegram-bot-token
ADMIN_IDS=123456789,987654321
NOTIFY_SECRET=your-secret-key
```

### 3. Запуск
```bash
# Автоматический запуск
./start.sh

# Или пошагово
make up
make migrate
make seed
```

### 4. Открытие
- 🌐 **Главная**: http://localhost
- 📦 **Товары**: http://localhost/products
- 🔧 **API**: http://localhost/api/
- 📊 **Админка**: http://localhost/admin
- 🤖 **Bot API**: http://localhost/notify/

## 🌐 Nginx проксирование

Все сервисы доступны через единый порт 80:

- **/** → Frontend (Next.js)
- **/api/** → Backend (Django)
- **/admin/** → Django Admin
- **/media/** → Медиа файлы
- **/notify/** → Telegram Bot API

## 🎨 Дизайн и UX

### Цветовая схема
- **Бренд-голубой**: #22A3CF
- **Текст**: #222 (основной), #666 (вторичный)
- **Кнопки/подвал**: #2b2b2b

### Компоненты
- **Header**: Логотип + навигация с голубой линией
- **ProductsSlider**: Горизонтальный слайдер с фото товаров
- **ProductList**: Шахматное расположение на десктопе
- **OrderModal**: Форма заказа с валидацией
- **Footer**: Контакты + меню с иконками

## 🔧 Основные команды

```bash
make up          # Запуск всех сервисов
make down        # Остановка
make logs        # Просмотр логов
make migrate     # Миграции БД
make seed        # Демо-данные
make test        # Тесты
make clean       # Полная очистка
```

## 📱 Адаптивность

- **Mobile-first** подход
- **Брейкпоинты** TailwindCSS
- **Шахматное расположение** товаров на десктопе
- **Колонка** на мобильных устройствах

## 🔒 Безопасность

- **HMAC SHA256** для уведомлений бота
- **Валидация** форм на фронтенде и бэкенде
- **CORS** настройки для API
- **Защита** от SQL-инъекций

## 🧪 Тестирование

```bash
# Запуск тестов
cd backend
python manage.py test

# Или через Docker
make test
```

## 📦 Технологии

- **Frontend**: Next.js 14, TypeScript, TailwindCSS
- **Backend**: Django 5, DRF, PostgreSQL
- **Bot**: aiogram 3, FastAPI
- **Infra**: Docker Compose, Nginx, PostgreSQL 15

## 🎯 Что дальше?

1. Добавьте реальные изображения товаров
2. Настройте Telegram бота с реальным токеном
3. Настройте домен и SSL
4. Добавьте аналитику и метрики
5. Реализуйте систему отзывов

---

**NartRental** - Профессиональная аренда оборудования для творческих проектов 🎬✨ 