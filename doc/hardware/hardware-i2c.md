# I2C configuration

### Downloading packages

```
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
```

### Configuring I2C
open raspi-config

```
sudo raspi-config
```
in graphic window, go to advanced tools, then enable automatic loading for I2C kernel module

### Adding modules to /etc/modules

```
echo "i2c-bcm2708" >> /etc/modules
echo "i2c-dev" >> /etc/modules
```
