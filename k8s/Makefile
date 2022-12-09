.PHONY: default
default:
	@echo Choose target


.PHONY: helm_install
helm_install:
	helm secrets install make-your-time ./make-your-time -n default -f ./mock-data.yaml

.PHONY:
helm_uninstall:
	helm uninstall make-your-time
