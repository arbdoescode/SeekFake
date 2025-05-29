#!/usr/bin/env bash

# Install ODBC prerequisites
apt-get update
apt-get install -y curl gnupg unixodbc-dev

# Add Microsoft package repo for ODBC 18
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Update again and install the driver
apt-get update
ACCEPT_EULA=Y apt-get install -y msodbcsql18

# Optional: Install sqlcmd if needed
ACCEPT_EULA=Y apt-get install -y mssql-tools18
