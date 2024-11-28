# Community Pulse Check: Streamlit Application

## Prerequisites

Before running the app, make sure you have the following prerequisites installed:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [MongoDB](https://www.mongodb.com/try/download/community)

## Installation


To run the app, clone the repository onto your local machine and create a new virtual environment:

```shell
git clone https://github.com/alan-turing-institute/teadt-community-survey.git
cd teadt-community-survey
conda create --name teadt-survey python=3.11
```

Start Docker Desktop then install the project dependencies:

```shell
make install-dependencies
make set-up-db
```


## Run the app 

```shell
run-local-container
```

## Azure SOPs

## Deploying a new app version

- It is important to check first a local deployment of the container works, to avoid debugging on App Service. You can do this with the `make run-local-container` command. 
- Before starting deployment, you will need to authenticate to the container registry. To obtain your credentials, use `az acr credential show --name teadt.azurecr.io`, and then use the values obtained in `docker login teadt.azurecr.io`
- To build an image an image and push it to Azure's Container registry, just run `make build-and-push-image`.
You will need to start Docker first, for the process to work.
- After the new version of the image was pushed (it can take a while), go the Azure Portal and stop and start [the `teadt` App Service](https://learn.microsoft.com/en-us/azure/spring-apps/enterprise/how-to-start-stop-delete?tabs=azure-portal). It can take a while for the change to be visible.

### Pausing the survey app

- Go to https://portal.azure.com/#home
- select resource 'teadt' of type 'App Service'
- On upper menu press Start/Stop
![Screenshot 2024-05-09 at 15 31 31](https://github.com/alan-turing-institute/teadt-community-survey/assets/6906140/1422a114-d744-450e-a5f4-1907fdbf38b3)

