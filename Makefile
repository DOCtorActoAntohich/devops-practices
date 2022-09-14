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

.PHONY: run_tests_local
run_tests_local:
	./venv/bin/python -m pytest tests
