FROM ubuntu:18.04
USER root
LABEL maintainer="izaidi"
WORKDIR /app
COPY . .
RUN mkdir -p /opt/results
ENTRYPOINT ["python3", "app.py"]
