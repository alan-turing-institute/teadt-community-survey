build-and-push-image:
	cd webapp && \
	docker buildx build --platform linux/amd64 -t teadtstreamlitlinux:latest -f Dockerfile .
	docker tag teadtstreamlitlinux:latest teadt.azurecr.io/teadtstreamlitlinux:latest && \
	docker push teadt.azurecr.io/teadtstreamlitlinux:latest

install-dependencies:
	cd webapp && python -m pip install -r requirements.txt -r dev-requirements.txt  

set-up-db:
	docker run --name mongodb -d mongodb/mongodb-community-server:latest

run-local-container:
	cd webapp && \
	docker build -t teadtstreamlitapp:latest -f Dockerfile .
	docker run --rm -it -p 8000:8000 -p 27017:27017 \
	 -e 'CONNECTION_STRING=mongodb://host.docker.internal:27017' -e 'DB_NAME=teadt_assurance' \
	 -e 'COLLECTION_NAME=assurance_survey' teadtstreamlitapp:latest
	
run-local:
	export CONNECTION_STRING=mongodb://127.0.0.1:27017 && \
	export DB_NAME=teadt_assurance && \
	export COLLECTION_NAME=assurance_survey && \
	streamlit run webapp/Home.py
	
run-type-checker:
	python -m mypy .

run-linter:
	python -m flake8

run-formatter:
	python -m black --line-length=79 .

	