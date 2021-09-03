################################################
#   Compile with:
#       docker build -t test-arg .
#       docker build -t test-arg --build-arg MY_NAME_ARG=Rafael .
#
#   Run with:
#       docker run --name container-arg test-arg
#
#################################################
FROM python:3

ARG MY_NAME_ARG=EDSON
ENV MY_NAME $MY_NAME_ARG

COPY arg.py /home/app/
WORKDIR /home/app

CMD [ "python", "-u", "arg.py" ]