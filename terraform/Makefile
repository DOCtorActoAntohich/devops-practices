.PHONY: list
.SILENT: list
list:
	echo Choose a target:
	grep -E '^[a-zA-Z0-9_-]+:' Makefile

.PHONY: run_local
run_local:
	cd local && \
	if ! [[ -d .terraform ]]; then terraform init; fi && \
	terraform apply

.PHONY: stop_local
stop_local:
	cd local && terraform destroy

.PHONY: run_yandex
run_yandex:
	cd yandex && \
	if ! [[ -d .terraform ]]; then terraform init; fi && \
	terraform apply

.PHONY: stop_yandex
stop_yandex:
	cd yandex && terraform destroy

.PHONY: create_yandex_token
create_yandex_token:
	yc iam create-token
