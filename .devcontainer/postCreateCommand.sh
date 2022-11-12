#!/bin/sh
set -e

composer --working-dir=/var/www/html --no-cache install
