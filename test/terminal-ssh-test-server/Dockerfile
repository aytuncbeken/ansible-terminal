FROM ubuntu
MAINTAINER Aytunc BEKEN aytuncbeken.ab@gmail.com
ENV SSH_USER=root

RUN apt-get update
RUN apt-get -yq install openssh-server
RUN mkdir -p /var/run/sshd
COPY sshd_config /etc/ssh/sshd_config
RUN /etc/init.d/ssh restart

#Set user specific ssh directory
RUN mkdir /$SSH_USER/.ssh && chmod 700 /$SSH_USER/.ssh
RUN touch /$SSH_USER/.ssh/authorized_keys

VOLUME /$SSH_USER/.ssh/
EXPOSE 22
