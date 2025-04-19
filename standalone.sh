#!/bin/bash

/lib/systemd/systemd-udevd --daemon
udevadm control --reload-rules
udevadm trigger

python standalone.py
