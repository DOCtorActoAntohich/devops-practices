.PHONY: default
.SILENT: default
default:
	echo Choose a target

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
