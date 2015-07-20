FROM docker/whalesay:latest

CMD /bin/bash

RUN yum install -y fortunes

CMD /usr/games/fortune -a | cowsay

