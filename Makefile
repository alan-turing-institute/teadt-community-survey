build-linux-image:
	cd webapp && \
	docker buildx build --platform linux/amd64 -t teadtstreamlitlinux:latest -f Dockerfile .

show-registry-credentials:
	az acr update -n teadt --admin-enabled true && \
	az acr credential show --name teadt.azurecr.io

tag-and-push-image:
	docker tag teadtstreamlitlinux:latest teadt.azurecr.io/teadtstreamlitlinux:latest && \
	docker push teadt.azurecr.io/teadtstreamlitlinux:latest