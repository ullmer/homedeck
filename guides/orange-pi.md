## OrangePi Zero 2W

### OrangePi OS (Ubuntu)

[Download](https://drive.google.com/drive/folders/1g806xyPnVFyM8Dz_6wAWeoTzaDg3PH4Z)

Install the `*_sever_linux version`. If kernel 6.1 doesn't work then try 5.4.

1. Burn the OS to the SD card
2. Plug in HDMI, USB Keyboard (middle port) and power (right-most port)
3. Default password is `orangepi`
4. Optional: run `apt update && apt upgrade`
5. Run `orangepi-config` and setup WiFi (same network as Home Assistant), timezone and SSH
6. Use [Terminal & SSH addon](https://github.com/hassio-addons/addon-ssh) to connect to the device (`ssh root@<ip>`, `orangepi` as password)
7. Run this command to install HomeDeck:  
  ```bash
  curl -fsSL https://raw.githubusercontent.com/redphx/homedeck/main/guides/linux/install.sh | bash
  ```
8. 

### Armbian (Debian)

[Download](https://www.armbian.com/orange-pi-zero-2w/)
