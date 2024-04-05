#!/usr/bin/env bash
# Set up server file system for deployment

# install nginx
apt-get -y update
apt-get -y install nginx
service nginx start

# configure file system
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Holberton School" | tee /data/web_static/releases/test/index.html > /dev/null
ln -sf /data/web_static/releases/test/ /data/web_static/current

# configure permissions
chown -R ubuntu:ubuntu /data/

# configure nginx
sudo sed -i '42i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# restart web server
service nginx restart
