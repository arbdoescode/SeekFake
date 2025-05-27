#!/usr/bin/env bash

set -e 

apt-get update && \
apt-get install -y curl gnupg2 apt-transport-https software-properties-common

curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

apt-get update && \
ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev gcc g++ libpq-dev

pip install --upgrade pip
pip install -r requirements.txt
