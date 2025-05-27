#!/usr/bin/env bash

# Update and install system dependencies
apt-get update && \
apt-get install -y curl gnupg2 gcc g++ libpq-dev unixodbc-dev

# Add Microsoft package repo and install the ODBC driver
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

apt-get update && \
ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Upgrade pip and install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
