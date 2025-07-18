#!/bin/bash
set -e

# Wait for DB to be ready
echo "Waiting for Postgres..."
while ! nc -z postgres 5432; do
  sleep 1
done

echo "Initializing Airflow DB..."
airflow db init

echo "Creating Airflow admin user..."
airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com

# Start the main Airflow process (passed from docker-compose)
exec airflow "$@"
