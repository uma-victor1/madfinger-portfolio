#!/bin/bash


set -e


PROJECT_DIR="/root/madfinger-portfolio"
SESSION_NAME="portfolio"


VENV_PATH="$PROJECT_DIR/python3-virtualenv"


echo "Killing all tmux sessions"

tmux kill-server || true


echo "Navigating to project directory"
cd "$PROJECT_DIR"


echo "Updating repository from GitHub"
# Fetch the latest changes and reset the local main branch to match the remote
git fetch
git reset origin/main --hard


echo "Installing Python dependencies"

source "$VENV_PATH/bin/activate"
pip install -r requirements.txt


echo "Starting new detached tmux session for the Flask app"

CMD="source \"$VENV_PATH/bin/activate\" && flask run --host=0.0.0.0"

# Create a new detached tmux section
# and run the command string inside it.
tmux new-session -d -s "$SESSION_NAME" "$CMD"



echo "Redeployment script finished successfully!"
