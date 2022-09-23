.PHONY: default
.SILENT: default
default:
	echo Choose a target

.PHONY: run_local
run_local:
	cd local && \
	if ! [[ -d ./local/.terraform ]]; then terraform init; fi && \
	terraform apply

.PHONY: stop_local
stop_local:
	cd local && terraform destroy
