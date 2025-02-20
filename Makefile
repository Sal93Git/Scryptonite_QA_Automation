IMAGE_NAME=your-dockerhub-username/your-image-name
TAG=latest

.PHONY: build push login

login:
	docker login

build:
	docker build -t $(IMAGE_NAME):$(TAG) .

push: login build
	docker push $(IMAGE_NAME):$(TAG)
