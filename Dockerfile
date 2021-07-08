FROM ubuntu:latest
USER root
RUN apt-get update 
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install -y git python3-pip

WORKDIR /app

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir -p /opt/results
ENTRYPOINT ["python3", "app.py"]
