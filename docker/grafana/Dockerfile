FROM centos:7
MAINTAINER "Federico Simoncelli" <fsimonce@redhat.com>

ADD fsimonce-heapster-epel-7.repo /etc/yum.repos.d/fsimonce-heapster-epel-7.repo
RUN yum -y install httpd grafana && yum clean all

EXPOSE 80

ADD grafana.conf /etc/httpd/conf.d/grafana.conf

ADD run-apache.sh /run-apache.sh
RUN chmod +x /run-apache.sh

CMD ["/run-apache.sh"]
