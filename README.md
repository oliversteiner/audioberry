# AudioBerry
https://docs.python-guide.org/writing/structure/#structure-of-the-repository



Install on Ubuntu
sudo apt install python-rpi.gpio python-gpiozero python3-gpiozero
pip3 install rpi.gpio
https://sourceforge.net/p/raspberry-gpio-python/tickets/165/
sudo apt install mercurial
pip3 install --upgrade hg+http://hg.code.sf.net/p/raspberry-gpio-python/code#egg=RPi.GPIO



# OLED Display
 display module is a 0.96″ I2C IIC SPI Serial 128X64 OLED LCD LED Display Module.
 
 https://github.com/adafruit/Adafruit_Python_SSD1306
 https://www.raspberrypi-spy.co.uk/2018/04/i2c-oled-display-module-with-raspberry-pi/

sudo apt install -y python-imaging python-smbus i2c-tools
sudo apt install -y python3-pil

sudo pip3 install --upgrade pip setuptools wheel
sudo pip3 install Adafruit-SSD1306


## Finding the OLED Display Module’s Address
i2cdetect -y 1
