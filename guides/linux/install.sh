# USB HID
apt install -y udev usbutils libusb-1.0-0-dev libudev-dev
# Python3 with venv support
apt install -y python3-venv
# Tools for HomeDeck
apt install -y libcairo2 optipng

mkdir -p /app
# Download HomeDeck
git clone https://github.com/redphx/homedeck.git

# Create custom venv
python3 -m venv /app/homedeck-venv
# Install HomeDeck
source /app/homedeck-venv/bin/activate && cd /app/homedeck && pip install -e .

# Run HomeDeck at startup
( crontab -l 2>/dev/null; echo "@reboot /bin/bash -c 'source /app/homedeck-venv/bin/activate && python /app/homedeck/server.py'" ) | crontab -

echo "Installed HomeDeck successfully!"
