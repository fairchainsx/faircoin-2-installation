# Installation Instruction faircoin on Docker environment and Raspberry Pi

### Preparation of Raspberry Pi
(tested on Raspberry Pi 3)

#### Install Ubuntu Server

##### Download Image ( on your desktop )
https://ubuntu.com/download/raspberry-pi

##### Check checksum of image ( on your desktop )
~~~
sha256sum ~/Downloads/ubuntu-19.10.1-preinstalled-server-arm64+raspi3.img.xz
~~~

##### Create installation media ( SD card ) ( on your desktop )
~~~
sudo dd of=/dev/mmcblk0 bs=32M
sync
~~~

Now you can put the SD card to Raspberry Pi and start the installation.

##### set keyboard ( optional )
~~~
# set keymap of the current session
sudo loadkeys de

# set keymap permanently
localectl set-keymap de
~~~

##### create swap memory
To build/make the faircoin app on Raspberry Pi it requires minimum of 2 GB memory size.
If the memory size of Raspberry Pi is lower than 2 GB then swap memory need to be created.
~~~
# Make all swap off
sudo swapoff -a

# Resize the swapfile
sudo dd if=/dev/zero of=/swapfile bs=1M count=1024

# Make swapfile usable
sudo mkswap /swapfile

# Make swapon again
sudo swapon /swapfile
~~~

#### Install Docker on Raspberry Pi
~~~
sudo apt install docker.io
~~~

Now you can follow the instructions  [installation_by_docker.md](installation_by_docker.md)

Notice: The creation on Raspberry Pi need some patience ( ~1.5 hour on Raspberry Pi 3 !! )
