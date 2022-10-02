.PHONY: list
.SILENT: list
list:
	echo Choose target:
	grep -E '^[a-zA-Z0-9_-]+:' Makefile

.PHONY: yandex_install_run
yandex_install_and_run:
	@export ANSIBLE_CONFIG=$(realpath ./ansible.cfg) && \
	ansible-playbook \
		-i ./inventory/dynamic/yandex.yaml \
		--diff \
		./playbooks/main.yaml

.PHONY: yandex_run_installed
yandex_run_installed:
	@export ANSIBLE_CONFIG=$(realpath ./ansible.cfg) && \
	ansible-playbook \
		-i ./inventory/dynamic/yandex.yaml \
		--diff \
		--extra-vars "setup_docker=false" \
		./playbooks/main.yaml

.PHONY: yandex_stop
yandex_stop:
	@export ANSIBLE_CONFIG=$(realpath ./ansible.cfg) && \
	ansible-playbook \
		-i ./inventory/dynamic/yandex.yaml \
		--diff \
		--extra-vars "wipe=true" \
		./playbooks/main.yaml

.PHONY: view_yandex_inventory
view_yandex_inventory:
	@export ANSIBLE_CONFIG=$(realpath ./ansible.cfg) && \
	ansible-inventory \
		-i ./inventory/dynamic/yandex.yaml \
		--list
