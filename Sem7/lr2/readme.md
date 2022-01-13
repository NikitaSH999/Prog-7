FROM python:3.8-slim
WORKDIR /home/app
COPY index.html index.html
RUN python3 -m http.server 8080