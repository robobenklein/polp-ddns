
.PHONY: up down

up:
	docker-compose up --build -d

down:
	docker-compose down

.PHONY: dev-up
dev-up:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d mongo

.PHONY: exec
exec:
	docker-compose exec flask bash

.PHONY: logs
logs:
	docker-compose logs -f

.PHONY: clean
clean:
	docker-compose down
	docker-compose rm
