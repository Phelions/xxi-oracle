#!/bin/sh

sudo sh -c "echo /opt/oracle/instantclient_19_3 > \
      /etc/ld.so.conf.d/oracle-instantclient.conf"
sudo ldconfig