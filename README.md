# DockerStuff

This repo was made to practice Docker commands.

## helloWorld
There is an python script which just prints _*Hello world!*_ and its Dockerfile to create an image in order to create a container and execute it.

## arguments
This script was created to test how to pass optional and positional arguments to the app in the container.

## environment
The `ENV` instruction sets the environment variable `<key>` to the value `<value>` so it can be accessed inside the script with `os.getenv()`.

## arg
The `ARG` instruction defines a variable that users can pass at build-time to the builder with the `docker build` command.
