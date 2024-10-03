# Run Example in "A Developer's Essential Guide to Docker Compose"

## Chapter 01

```sh
docker build -t custom-nginx:0.1 .
docker compose up

```

## Chapter 02

```sh
docker build . -t task-manager:0.1
docker compose up -d
docker compose up --force-recreate 

```

## Chapter 03

```sh
docker compose up
docker network ls

```

## Chapter 04

```sh
docker compose up --no-start
docker ps -a
docker compose up --no-build -d
docker compose up --remove-orphans

docker compose exec task-manager ls
docker compose pause task-manager
docker compose unpause task-manager

docker compose ps
docker compose ps --services

docker compose images
docker compose down

docker compose up -d
docker compose logs
docker compose top

docker compose config

```

## Chapter 05

```sh
docker compose -f redis.yaml up -d
docker compose -f my-compose.yaml up -d

docker compose up
docker compose down
```

## Chapter 06

```sh
docker compose -f my-compose.yaml up -d

docker compose build
docker compose up -d


```

## Chapter 07

```sh
# Task Manager base
docker compose -f base-compose.yaml up -d
docker compose -f base-compose.yaml ps
docker compose -f base-compose.yaml down

# Combining Compose files
docker compose -f base-compose.yaml -f monitoring/docker-compose.yaml \
-f event-service/docker-compose.yaml -f location-service/docker-compose.yaml \
-f task-manager/docker-compose.yaml up

docker compose -f base-compose.yaml -f monitoring/docker-compose.yaml \
-f event-service/docker-compose.yaml -f location-service/docker-compose.yaml \
-f task-manager/docker-compose.yaml down

# Mock location service
docker compose -f base-compose.yaml -f task-manager/docker-compose.yaml \
-f location-service/mock-location-service.yaml up

docker compose -f base-compose.yaml -f task-manager/docker-compose.yaml \
-f location-service/mock-location-service.yaml down

# Mock Pushgateway
docker compose -f base-compose.yaml -f event-service/docker-compose.yaml \
-f monitoring/mock-push-gateway.yaml up

docker compose -f base-compose.yaml -f event-service/docker-compose.yaml \
-f monitoring/mock-push-gateway.yaml down

# Running with capturing enabled
docker compose -f base-compose.yaml -f monitoring/docker-compose.yaml \
-f event-service/capture-traffic-docker-compose.yaml \
-f location-service/docker-compose.yaml \
-f task-manager/capture-traffic-docker-compose.yaml \
-f hoverfly/proxy.yaml up

# Running applications individually

## Task Manager
docker compose -f base-compose.yaml -f location-service/mock-location-service.yaml -f task-manager/docker-compose.yaml
## Location service
docker compose -f base-compose.yaml -f location-service/docker-compose.yaml 
## Event service
docker compose -f base-compose.yaml -f monitoring/mock-push-gateway.yaml -f event-service/docker-compose.yaml

## Prometheus
docker compose -f base-compose.yaml -f monitoring/docker-compose.yaml

# Using config
docker compose -f base-compose.yaml -f location-service/docker-compose.yaml config



```

## Chapter 08

```sh
# Local DynamoDB
docker compose -f dynamo-compose.yaml up

# SQS locally
docker compose -f sqs-compose.yaml up

# Newsletter Run
docker compose -f docker-compose.yaml -f newsletter-lambda/docker-compose.yaml build
docker compose -f docker-compose.yaml -f newsletter-lambda/docker-compose.yaml up

# Test
curl -XPOST "http://localhost:8080/2015-03-31/functions/function/invocations" \
-d '{"email":"john@doe.com","topic":"Books"}'
"You have been subscribed to the Books newsletter"

## Error -- Problems in DynamoDB Table Init

docker compose -f docker-compose.yaml -f newsletter-lambda/docker-compose.yaml down

```

## Chapter 09

```sh
# Github Action Part is missing


```

## Chapter 10

```sh
DOCKER_HOST="ssh://cskim@192.168.70.116" docker run -it --rm redis

# Not working

```