#!/bin/bash

set -e

COMPOSE_FILE="docker-compose-dev.yml"

echo "Stopping and removing containers..."
docker-compose -f $COMPOSE_FILE down

echo "Rebuilding images..."
docker-compose -f $COMPOSE_FILE build

echo "Starting containers..."
docker-compose -f $COMPOSE_FILE up