REGISTRY ?= kubes1:5000
IMAGENAME ?= invoker:1.0.0
INVOKER_IMAGE ?= $(REGISTRY)/$(IMAGENAME)

.PHONY: all tag
all:
	sudo ./gradlew :core:invoker:distDocker
	sudo docker tag whisk/invoker:latest $(INVOKER_IMAGE)
	sudo docker push $(INVOKER_IMAGE)
	kubectl rollout restart sts/owdev-invoker -nopenwhisk

tag:
	sudo docker tag whisk/invoker:latest $(INVOKER_IMAGE)
	sudo docker push $(INVOKER_IMAGE)
