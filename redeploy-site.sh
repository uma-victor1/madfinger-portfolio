#!/bin/bash


set -e


PROJECT_DIR="/root/madfinger-portfolio"
SESSION_NAME="portfolio"


VENV_PATH="$PROJECT_DIR/python3-virtualenv"


echo "Navigating to project directory"
cd "$PROJECT_DIR"


echo "Updating repository from GitHub"
# Fetch the latest changes and reset the local main branch to match the remote
git fetch
git reset origin/main --hard


echo "Docker Compose"

docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build

echo "Redeployment script finished successfully!"
