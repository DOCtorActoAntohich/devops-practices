.PHONY: default
default: run_tests_local

.PHONY: build_and_run_local
build_and_run_local:
	docker build -t make_your_time -f ./docker/Dockerfile .
	docker run -d -p 8000:8000 --rm --name make_your_time make_your_time

.PHONY: run_from_remote
run_from_remote:
	docker run -d -p 8000:8000 --rm --name make_your_time doctoractoantohich/make_your_time

.PHONY: stop_app
stop_app:
	docker stop make_your_time

.PHONY: run_tests
run_tests:
	docker compose -f=docker-compose-test.yaml up --build --abort-on-container-exit --attach make_your_time_tests
	docker compose -f=docker-compose-test.yaml down -v

.PHONY: run_linter
run_linter:
	flake8 .

.PHONY: monitoring_compose_up
monitoring_compose_up:
	docker compose -f monitoring/docker-compose.yaml up -d

.PHONY: monitoring_compose_down
monitoring_compose_down:
	docker compose -f monitoring/docker-compose.yaml down
