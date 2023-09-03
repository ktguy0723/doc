yum localinstall https://dev.mysql.com/get/mysql80-community-release-el7-5.noarch.rpm -y

yum install mysql-community-server -y 

systemctl start mysqld

systemctl enable mysqld

cat /var/log/mysqld.log | grep localhost

mysql –u root -p

ALTER USER root@localhost IDENTIFIED BY ‘パスワード’;

create database udemy;

show databases;



Cannot open:https://dev.mysql.com/get/mysql80-community-release-el7-5.noarch.rpm. Skipping.

Nothing to do.というエラーが発生する場合は、以下のコマンドを実行してみてください。

wget https://dev.mysql.com/get/mysql80-community-release-el7-7.noarch.rpm






#!/bin/bash
# サーバーの設定変更
sed -i 's/^HOSTNAME=[a-zA-Z0-9\.\-]*$/HOSTNAME=udemy-bash/g' /etc/sysconfig/network
hostname 'udemy-bash'
cp /usr/share/zoneinfo/Japan /etc/localtime
sed -i 's|^ZONE=[a-zA-Z0-9\.\-\"]*$|ZONE="Asia/Tokyo"|g' /etc/sysconfig/clock
echo "LANG=ja_JP.UTF-8" > /etc/sysconfig/i18n

# アパッチのインストール （ユーザーデータはルートユーザーで実行されるためSudoはなくても実行可能：また、つけても実行可能です。）
yum update -y
yum install httpd -y 
====