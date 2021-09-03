################################################
#   Compile with:
#       docker build -t test-env .
#
#   Run with:
#       docker run --name container-env test-env
#       docker run --name container-env1 --env MY_NAME=Rafael test-env
#
#################################################
FROM python:3

ENV MY_NAME "Edson"

COPY variables.py /home/app/
WORKDIR /home/app

CMD [ "python", "-u", "variables.py" ] 