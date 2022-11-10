#!/bin/sh
set -e

composer --working-dir=/var/www/html --no-cache update

curl -L https://github.com/Croydon/blog-assets/archive/refs/heads/main.tar.gz | tar -xz --strip-components=1 -C /var/www/html/assets

service apache2 start
