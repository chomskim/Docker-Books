### README

This directory contains the source code for the first exercise of chapter 4. At the start of the chapter, we introduced a simple Dockerfile that did not build due to syntax errors. Here, you’ll fix the Dockerfile and add some of the instructions that you learned about in this chapter.

```
cd docker-hello-world/
docker build .

docker image ls
REPOSITORY    TAG       IMAGE ID       CREATED              SIZE
<none>        <none>    64cd0d166f9b   About a minute ago   48.2MB
hello-world   latest    d2c94e258dcb   12 months ago        13.3kB

docker run 64cd0d166f9b
Hello, CS Kim!

docker tag 64cd0d166f9b cskim/hello-world

docker image ls
REPOSITORY          TAG       IMAGE ID       CREATED         SIZE
cskim/hello-world   latest    64cd0d166f9b   7 minutes ago   48.2MB
hello-world         latest    d2c94e258dcb   12 months ago   13.3kB
```