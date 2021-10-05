.PHONY: venv
venv:
	pipenv install
	pipenv shell

.PHONY: docker
docker:
	docker build -f Dockerfile . -t lxc-proxy