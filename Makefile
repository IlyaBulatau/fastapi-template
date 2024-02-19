run:
	docker compose up

stop:
	docker stop $$(docker ps -q)

remove:
	docker container prune -f

upgrade_requirements:
	poetry export --without-hashes --format=requirements.txt > src/requirements.txt
