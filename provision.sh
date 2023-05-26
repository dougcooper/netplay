#!/bin/bash
sudo apt update
sudo apt install -y \
    tcpreplay pip python3-venv \
    gstreamer1.0-{pipewire,tools,plugins-{base,good,bad,ugly}} libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev gstreamer1.0-plugins-base-apps

sudo setcap cap_net_raw=eip "$(realpath "$(which python3)")"
sudo setcap cap_net_raw=eip "$(which tcpreplay)"