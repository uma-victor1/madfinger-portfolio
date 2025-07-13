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


echo "Installing Python dependencies"

source "$VENV_PATH/bin/activate"
pip install -r requirements.txt


echo "restarting my portfolio service for the Flask app"

systemctl daemon-reload
systemctl restart portfolio
systemctl status portfolio

echo "Redeployment script finished successfully!"
