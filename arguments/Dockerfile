################################################
#   Compile with:
#       docker build -t test-args .
#
#   Run with:
#       docker run --name container-args test-args -u edson.user
#       docker run --name container-args test-args extra.arg
#
#################################################
FROM python:3

COPY args.py /home/app/
WORKDIR /home/app

ENTRYPOINT [ "python", "-u", "args.py" ] 