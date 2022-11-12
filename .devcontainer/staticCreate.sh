#!/bin/sh
set -e

rm -rf /var/www/html/static
mkdir -p /var/www/html/static

wget -r -l="inf" -N --no-verbose --convert-links --adjust-extension --directory-prefix="/var/www/html/static" --no-host-directories "http://localhost"

cp config/CNAME /var/www/html/static/CNAME

cd /var/www/html/static/
python /var/www/html/.devcontainer/replace-urls.py

ls -la /var/www/html/static
