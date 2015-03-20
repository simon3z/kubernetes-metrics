FROM centos:7
MAINTAINER "Federico Simoncelli" <fsimonce@redhat.com>

ADD fsimonce-heapster-epel-7.repo /etc/yum.repos.d/fsimonce-heapster-epel-7.repo
RUN yum -y install heapster && yum clean all

# Pass in flags to heapster. Options: "--coreos", "--vmodule=*=4", etc.
ENV FLAGS ""

# Select what source sink to use. Options: "influxdb,gcm"
ENV SINK ""

ADD run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
