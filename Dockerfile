FROM ubuntu:16.04
ADD . /home/app
WORKDIR /home/app
RUN apt-get update \
    && apt-get install -y python3 python3-dev python3-pip \
    && pip3 install --upgrade pip \
    && pip3 install -r requirements.txt \
    && apt-get autoremove -y \
    && apt-get clean

#CMD ["python3", "run.py"]
CMD ["/bin/bash"]