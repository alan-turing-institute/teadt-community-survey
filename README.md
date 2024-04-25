# TEA-DT Survey App

This is a repository for a demo web app built using [streamlit](https://streamlit.io).


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
