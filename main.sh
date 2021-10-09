#!/bin/bash
# docker pull debian
# docker run -p 8000:8000/tcp -p 8080:8080/tcp -it debian bash
docker build -t letsencrypt .
docker run -p 8000:8000/tcp -p 8080:8080/tcp -it -d letsencrypt
