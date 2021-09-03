The docker build command builds Docker images from a Dockerfile

`docker build -t [name:tag] .`


The docker run command first creates a writeable container layer over the specified image, and then starts it using the specified command

`docker run -d --name test-hello -it test-hello`
`docker run -d --name test-hello -it test-hello bash`


The docker exec command runs a new command in a running container

`docker exec -it test-hello bash`


Dockerfile:

``` dockerfile
FROM ubuntu
RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN pip install pymongo
RUN pip install paho-mqtt
RUN apt-get install -y nano
COPY \app\ /home/code
WORKDIR /home/code/
CMD python -u verificador.py rangos.json ```
