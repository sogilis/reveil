# I2C configuration

### Downloading packages

	sudo apt-get install python-smbus -y


### Configuring I2C

Open raspi-config with the command **`sudo raspi-config`**.

in graphic window, go to **`Advanced Options`**, then enable automatic loading for I2C kernel module : **A7 I2C**, click OK or Yes for all, and then finish.


### Adding modules to /etc/modules

In the file /etc/modules, add the two following lines in sudo mode:

		i2c-bcm2708
		i2c-dev

Then reboot the raspberry.

You can now check the i2c enabling with the command `sudo i2cdetect -y 1` (in some cases `sudo i2cdetect -y 0`).

