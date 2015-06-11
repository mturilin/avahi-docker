FROM ubuntu:14.04

MAINTAINER Mikhail Turilin
# installing prerequisites
RUN apt-get update && apt-get install -y \
    curl \
    python-pip \
    avahi-daemon \
    libnss-mdns


RUN pip install j2cli PyYAML


# copying configuration
COPY *.service /root/
COPY avahi-daemon.conf /etc/avahi/

# copying prerun file
COPY config.py /usr/bin/config.py
RUN chmod +x /usr/bin/config.py

#EXPOSE 8888
#EXPOSE 55555

CMD /usr/bin/config.py && avahi-daemon