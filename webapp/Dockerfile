# webapp/Dockerfile

FROM python:3.10-slim

EXPOSE 8000
# Check if the line below is necessary
EXPOSE 27017 

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /webapp

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY  . .

RUN pip3 install -r requirements.txt

HEALTHCHECK CMD curl --fail http://localhost:8000/_stcore/health

ENTRYPOINT ["streamlit", "run", "home.py", "--server.port=8000", "--server.address=0.0.0.0"]