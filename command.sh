#! /bin/bash

echo "A cleaning will be carried out"
docker compose -f docker/docker-compose.yml down 

echo "Update the images"
docker compose -f docker/docker-compose.yml build --no-cache crypto-note-ia

echo "Starting the containers"
docker compose -f docker/docker-compose.yml --env-file .env up -d