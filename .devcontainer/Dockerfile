ARG PHP_VERSION=7.4
FROM php:${PHP_VERSION}-apache

ENV DEBIAN_FRONTEND=noninteractive
ENV COMPOSER_ALLOW_SUPERUSER=1

RUN apt-get update \
  && apt-get -y --no-install-recommends install git zip unzip wget python3 \
  && update-alternatives --install /usr/bin/python python /usr/bin/python3 10 \
  && curl -sSL https://getcomposer.org/installer | php \
  && chmod +x composer.phar \
  && mv composer.phar /usr/local/bin/composer \
  && rm /etc/apache2/sites-enabled/000-default.conf \
  && ln -s /var/www/html/config/apache-site-config.conf /etc/apache2/sites-enabled/000-default.conf \
  && a2enmod rewrite \
  && chown -R www-data:www-data /var/www/html \
  && apt-get autoremove -y \
  && apt-get clean -y \
  && rm -rf /var/lib/apt/lists/*

ENV DEBIAN_FRONTEND=dialog

EXPOSE 80
