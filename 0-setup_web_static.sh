#!/usr/bin/env bash
# Script to setup Web 1 & Web 2 servers to serve static content
FAKE_HTML="<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>"
SERVER_BLOCK_PATH="/etc/nginx/sites-available/default"
ROOT_DIR="/data"
RELEASES="$ROOT_DIR/web_static/releases/test"
SHARED="$ROOT_DIR/web_static/shared"
LINK="$ROOT_DIR/web_static/current"
STATIC="\n\tlocation /hbnb_static/ {\n\t\talias $LINK/;\n\t}\n"

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p "$RELEASES" "$SHARED"
echo -e "$FAKE_HTML" | sudo tee "$RELEASES/index.html"
sudo ln -sf "$RELEASES" "$LINK"
sudo chown -hR ubuntu:ubuntu "$ROOT_DIR"
sudo sed -i "46 a\ $STATIC" "$SERVER_BLOCK_PATH"
sudo service nginx restart
