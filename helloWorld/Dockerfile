################################################
# Compile with:
#     docker build -t test-hello .
#
# Run with:
#     docker run --name test-container test-hello
#
#################################################
FROM python:3

COPY . /home/app
WORKDIR /home/app

CMD [ "python", "-u", "helloWorld.py" ] 