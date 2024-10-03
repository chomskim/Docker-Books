### README

This directory contains the source code for the second exercise of chapter 4. In this exercise, you will build two Docker images

 - Using the standard build process using python:3 as the base image (present in [docker-multi-stage/standard-build](docker-multi-stage/standard-build) directory. 
 - Using Multi-Stage builds (present [docker-multi-stage/multistage-build](docker-multi-stage/multistage-build) directory. 

```
cd multistage-build
docker build .
docker image ls
REPOSITORY          TAG       IMAGE ID       CREATED             SIZE
<none>              <none>    e8521a7bf742   28 seconds ago      58.8MB
cskim/hello-world   latest    64cd0d166f9b   About an hour ago   48.2MB
hello-world         latest    d2c94e258dcb   12 months ago       13.3kB

docker tag e8521a7bf742 cskim/multistage-build
docker image ls
REPOSITORY               TAG       IMAGE ID       CREATED             SIZE
cskim/multistage-build   latest    e8521a7bf742   6 minutes ago       58.8MB
cskim/hello-world        latest    64cd0d166f9b   About an hour ago   48.2MB
hello-world              latest    d2c94e258dcb   12 months ago       13.3kB
```
