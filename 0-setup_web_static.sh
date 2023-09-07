#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.
# Update the package list and install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create the necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html><head></head><body>Web Static Test</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate the symbolic link
sudo rm -f /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
alias_config="location /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n"

# Check if alias_config is already in the nginx_config
if ! grep -q "alias /data/web_static/current/;" "$nginx_config"; then
    sudo sed -i "/server_name _;/a $alias_config" "$nginx_config"
fi

# Restart Nginx
sudo service nginx restart
