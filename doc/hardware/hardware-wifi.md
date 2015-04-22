# TP-Link TL-WN725N Wifi dongle configuration

**prerequisite : The Wifi dongle shall not be plugged.**

### Retrieve Linux kernel version

```
uname -a
```

### Download

- The following has only be tested with Raspberry Pi kernel version **3.18.11+**
- Download the driver archive [here](https://www.raspberrypi.org/forums/viewtopic.php?p=462982#p462982) corresponding to the kernel version

### Installation

The following assumes the driver archive is of the form `8188eu-yyyymmdd.tar.gz`. From the Raspberry Pi,

```
tar xzf 8188eu-yyyymmdd.tar.gz
./install.sh
# Insert the dongle onto one of the Raspberry Pi USB ports.
sudo reboot

```

After a reboot, `ifconfig` command should now prompt a `wlan0` interface and `lsmod` should now show a `8188eu` module currently running.

### Wireless network configuration

Edit `/etc/network/interfaces` and set it to the following content:

```
auto lo
iface lo inet loopback

allow-hotplug eth0
iface eth0 inet dhcp

auto wlan0                  # Allow wlan0 to be started at boot time.
allow-hotplug wlan0
iface wlan0 inet dhcp

wpa-ssid "NETWORK-NAME"     # Set the SSID of the access point here.
wpa-psk  "NETWORK-PASSWORD" # Set the PSK key of the access point here.
```
