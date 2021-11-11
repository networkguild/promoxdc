IMAGE := laurihuotari/lxc-proxy
TAG ?= latest
VERSION_NUMBER := sha-$(shell git rev-parse HEAD 2> /dev/null)

.PHONY: venv
venv:
	pipenv install
	pipenv shell

.PHONY: docker
docker:
	docker build -f Dockerfile . -t $(IMAGE):$(TAG) --build-arg VERSION=$(VERSION_NUMBER)

.PHONY: publish
publish: docker
	docker push $(IMAGE):$(TAG)
