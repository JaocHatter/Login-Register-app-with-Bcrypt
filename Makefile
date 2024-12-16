run:
	docker compose up

reset:
	docker compose up --build

test:
	pytest

.PHONY: run test reset