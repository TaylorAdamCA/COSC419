#!/bin/bash

yes Y | sudo yum install python-pip
yes Y | sudo pip install --upgrade pip
yes Y | sudo pip install flask
yes Y | sudo curl --fail -sSLo /etc/yum.repos.d/passenger.repo https://oss-binaries.phusionpassenger.com/yum/definitions/el-passenger.repo
yes Y | sudo yum install -y mod_passenger || sudo yum-config-manager --enable cr && sudo yum install -y mod_passenger
sudo mkdir /var/www/lab8
cp -r * /var/www/lab8
cp myapp_cpy.conf /etc/httpd/conf.d/myapp.conf
sudo service httpd restart
