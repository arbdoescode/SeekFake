FROM python:3.11-slim

# Install base packages and Microsoft ODBC Driver dependencies
RUN apt-get update && \
    apt-get install -y curl gnupg2 software-properties-common apt-transport-https unixodbc-dev gcc g++ && \
    mkdir -p /etc/apt/keyrings && \
    curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/keyrings/microsoft.gpg && \
    echo "deb [signed-by=/etc/apt/keyrings/microsoft.gpg] https://packages.microsoft.com/debian/11/prod bullseye main" > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 6969
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6969"]
