.PHONY: list
.SILENT: list
list:
	echo Choose target:
	grep -E '^[a-zA-Z0-9_-]+:' Makefile

.PHONY: run_yandex_playbook
run_yandex_playbook:
	@export ANSIBLE_CONFIG=$(realpath ./ansible.cfg) && \
	ansible-playbook -i ./inventory/dynamic/yandex.yaml ./playbooks/main.yaml --diff

.PHONY: view_yandex_inventory
view_yandex_inventory:
	@export ANSIBLE_CONFIG=$(realpath ./ansible.cfg) && \
	ansible-inventory -i ./inventory/dynamic/yandex.yaml --list
