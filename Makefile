.PHONY: up down logs migrate createsuperuser seed clean test

up:
	docker-compose -f deploy/docker-compose.yml --env-file .env up -d

down:
	docker-compose -f deploy/docker-compose.yml --env-file .env down

logs:
	docker-compose -f deploy/docker-compose.yml --env-file .env logs -f

migrate:
	docker-compose -f deploy/docker-compose.yml --env-file .env exec backend python manage.py migrate

createsuperuser:
	docker-compose -f deploy/docker-compose.yml --env-file .env exec backend python manage.py createsuperuser

seed:
	docker-compose -f deploy/docker-compose.yml --env-file .env exec backend python manage.py seed_data

test:
	docker-compose -f deploy/docker-compose.yml --env-file .env exec backend python manage.py test

clean:
	docker-compose -f deploy/docker-compose.yml --env-file .env down -v
	docker system prune -f

status:
	@echo "🌐 Главная: http://localhost"
	@echo "📦 Товары: http://localhost/products"
	@echo "🔧 API: http://localhost/api/"
	@echo "📊 Админка: http://localhost/admin"
	@echo "🤖 Bot API: http://localhost/notify/" 