### README

This directory contains the source code for the first exercise of chapter 5. In this exercise, we build an nginx Docker image with a Docker volume attached, which contains a custom nginx configuration. Toward the second part of the exercise, we will attach a bind mount and a volume containing a static web page and a custom nginx configuration. The intent of the exercise is help the readers understand how to leverage volumes and bind mounts to make local development easy.

```
docker build -t cskim/nginx-volume .

docker image ls
REPOSITORY               TAG       IMAGE ID       CREATED          SIZE
cskim/nginx-volume       latest    b2a9bb522691   14 seconds ago   48.3MB
cskim/newsbot            latest    aae749ca3254   7 hours ago      58.7MB

docker run -d --name nginx-volume -p 8080:80 cskim/nginx-volume

docker stop nginx-volume

docker run -d --name nginx-volume-bind -v "$(pwd)"/:/srv/www -p 8080:80 cskim/nginx-volume

docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS          PORTS                                   NAMES
7fca811c5660   cskim/nginx-volume   "/docker-entrypoint.…"   28 seconds ago   Up 24 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   nginx-volume-bind

docker inspect nginx-volume-bind | jq ".[].Mounts"
[
  {
    "Type": "bind",
    "Source": "/home/cskim/docker-project/upenn-app/practical-docker-with-python/source-code/chapter-5/exercise-1/docker-volume-bind-mount",
    "Destination": "/srv/www",
    "Mode": "",
    "RW": true,
    "Propagation": "rprivate"
  },
  {
    "Type": "volume",
    "Name": "84a8c61b32418c18cf7daf70450da90bdd732e8614a763944ad1cbfbc618e568",
    "Source": "/var/lib/docker/volumes/84a8c61b32418c18cf7daf70450da90bdd732e8614a763944ad1cbfbc618e568/_data",
    "Destination": "/var/lib",
    "Driver": "local",
    "Mode": "",
    "RW": true,
    "Propagation": ""
  }
]


```