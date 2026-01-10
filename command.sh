#! /bin/bash

echo "A cleaning will be carried out"
docker compose down 

echo "Update the images"
docker compose --env-file ./.env up -d --build --remove-orphans

echo "Starting the containers"
docker compose --env-file .env up -d