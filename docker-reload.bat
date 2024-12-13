@echo off

echo Rebuilding Docker image...
docker-compose build

echo Reloading Docker Compose services...
docker-compose up -d db 
docker-compose up -d phpmyadmin 
docker-compose up -d python

echo Displaying logs for the services...
docker-compose logs -f
