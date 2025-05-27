#!/usr/bin/env bash

set -e  # Stop the script if any command fails

# Install prerequisites
apt-get update
apt-get install -y curl gnupg2 apt-transport-https software-properties-common

# Add Microsoft package signing key
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Add Microsoft SQL Server repository (for Debian 11/Ubuntu 20+)
curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Update and install ODBC Driver 18
apt-get update
ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev gcc g++ libpq-dev

# Upgrade pip and install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
