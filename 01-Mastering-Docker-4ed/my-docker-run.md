# Chapter 02

```sh
cd 01-dockerfile-example
docker build --tag local:dockerfile-example .
docker run -d --name dockerfile-example -p 8080:80 local:dockerfile-example
docker stop dockerfile-example
docker rm dockerfile-example

docker run --name nginx-version local:dockerfile-example -v
nginx version: nginx/1.26.2

docker image inspect -f {{.Config.Labels}} local:dockerfile-example
map[description:This example Dockerfile installs NGINX. maintainer:Russ McKendrick <russ@mckendrick.io>]

docker stop dockerfile-example
docker rm dockerfile-example nginx-version

docker image pull alpine:latest
docker run -it --rm --name alpine-test alpine /bin/sh
/ # apk update
/ # apk upgrade
/ # apk add --update nginx
/ # rm -rf /var/cache/apk/*
/ # mkdir -p /tmp/nginx/
/ # exit

docker commit alpine-test local:broken-container
docker image save -o broken-container.tar local:broken-container

cd ../02-scratch-example
docker build --tag local:fromscratch .
docker rm alpine-test
docker run -it --rm --name alpine-test local:fromscratch /bin/sh
/ # cat /etc/*release
3.11.3
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.11.3
PRETTY_NAME="Alpine Linux v3.11"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://bugs.alpinelinux.org/"
/ # exit

cd ../03-env-example/

docker build --tag local/apache-php:7 .
docker run -d -p 8080:80 --name apache-php7 local/apache-php:7

docker build --tag local/apache-php:5 .
docker run -d -p 9090:80 --name apache-php5 local/apache-php:5

docker images
REPOSITORY         TAG                  IMAGE ID       CREATED              SIZE
local/apache-php   5                    3142b6400869   About a minute ago   44.5MB
local/apache-php   7                    075bb4e3f14e   5 minutes ago        21.2MB
...

cd ../05-multi-stage/
docker build --tag local:go-hello-world .
docker run -d --rm -p 8000:80 --name go-hello-world local:go-hello-world
docker stop go-hello-world
docker rm go-hello-world

```

# Chapter 03

```sh
docker image pull masteringdockerfouthedition/dockerfile-example:latest
docker images
docker run -d -p8080:80 --name example masteringdockerfouthedition/dockerfile-example
docker stop example go-hello-world
docker rm example go-hello-world

```

# Chapter 04

```sh
docker image pull redis:alpine
docker image pull russmckendrick/moby-counter
docker network create moby-counter-net
docker run -d --rm --name redis --network moby-counter-net redis:alpine
docker run -d --rm --name moby-counter --network moby-counter-net \
-p 8080:80 russmckendrick/moby-counter
docker exec moby-counter ping -c 3 redis
docker inspect moby-counter-net

docker stop redis

docker container run -d --rm --name redis -v redis_data:/data \
--network moby-counter-net redis:alpine
docker inspect redis_data

docker stop redis moby-counter
docker container prune
docker network prune
docker volume prune

```

# Chapter 05

```sh
cd 01-mobycounter/
docker compose up
docker compose down

cd ../02-example-voting-app/

# Using dotnet
# Change worker Dockerfile
# FROM microsoft/dotnet:2.0.0-sdk ==>
# FROM mcr.microsoft.com/dotnet/sdk:6.0

# Change worker/dotnet/.../Worker.csproj
#   <PropertyGroup>
#     <OutputType>Exe</OutputType>
#     <TargetFramework>netcoreapp2.2</TargetFramework>
#     <CheckEolTargetFramework>false</CheckEolTargetFramework>
#   </PropertyGroup>

docker compose up

# Still Not working
# 
# worker-1  | Could not execute because the specified command or file was not found.
# worker-1  | Possible reasons for this include:
# worker-1  |   * You misspelled a built-in dotnet command.
# worker-1  |   * You intended to execute a .NET program, but dotnet-src/Worker/Worker.dll does not exist.
docker compose down

docker image  prune -a
# Using Java
docker compose -f docker-compose-javaworker.yml up

docker compose -f docker-compose-javaworker.yml down
# It works!!

```

# Chapter 09 -- Run portainer

```sh
docker image pull portainer/portainer
docker volume create portainer_data
docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer

# http://localhost:9000
# admin Passw0rd1234

```