FROM ubuntu:18.04
RUN mkdir /code
COPY requirments.txt /code/
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev
RUN pip3 install -r code/requirments.txt
COPY ./backMessenger /code/

#ENTRYPOINT [ "python3", "code/manage.py", "runserver"]