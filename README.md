# AtariSTSongPlayer
Endless Atari ST Chip Tune player for installing on a Raspberry Pi in a car.

Run Raspberry Pi OS on a Pi 3 Model A+.

Install build tools:
```
sudo apt-get install cmake g++ libao-dev xxd libasound2-dev
```

Download and compile PSG play (with ALSA support) from https://github.com/frno7/psgplay with:
```
git clone --recurse-submodules https://github.com/frno7/psgplay.git
cd psgplay/
make ALSA=1 psgplay
```
Download the SNDH Atari ST YM2149 archive from https://sndh.atari.org/
Extract it to /home/pi/music

Install pigpio to listen to the GPIO pins
```
sudo apt-get install pigpio
sudo systemctl enable pigpiod
sudo systemctl start pigpiod
```

Install python if using an LCD display for track names:
```
sudo apt-get install python
```
Connect a Waveshare LCD1602 LCD display to pins 3, 4, 5, 6 (GPIO 2 I2C1 SDA, 5V power, GPIO 3 I2C SCL, Ground) as per
https://www.waveshare.com/wiki/LCD1602_I2C_Module_(Blue)

Place Songname.py from this repo in 
```
/home/pi/Songname.py
```

Place psgplay_start.sh from this repo in
```
/home/pi/psgplay_start.sh
```
Set it as executable
```
chmod +x psgplay_start.sh
```
Set the script up as a service to run at boot, create /etc/systemd/system/psgplay.service as below:
```
[Unit]
Description=Play random Atari ST tunes using PSGPlay
After=multi-user.target
[Service]
ExecStart=/home/pi/psgplay_start.sh
WorkingDirectory=/home/pi
StandardOutput=journal
StandardError=journal
Restart=always
User=pi
Group=pi
[Install]
WantedBy=multi-user.target
```
Set the Raspberry Pi to read only mode to protect against sudden loss of power in a car
```
sudo nano /etc/fstab
```
change
```
PARTUUID=xxxxxxx / ext4 defaults,noatime 0 1
```
to
```
PARTUUID=xxxxxxx / ext4 defaults,noatime,ro 0 1
tmpfs /tmp tmpfs defaults,noatime,size=50M 0 0
tmpfs /var/tmp tmpfs defaults,noatime,size=10M 0 0
tmpfs /var/log tmpfs defaults,noatime,size=10M 0 0
tmpfs /var/lib/dhcp tmpfs defaults,noatime,size=1M 0 0
tmpfs /var/lib/dhcpcd5 tmpfs defaults,noatime,size=1M 0 0
tmpfs /run tmpfs defaults,noatime,size=10M 0 0
```
Disable logging to SD card
```
sudo systemctl disable rsyslog
sudo systemctl disable systemd-journald
```


Wire up a switch between GPIO 26 (pin 37) and GND (pin 39) on your Raspberry Pi

Connect the 3.5mm audio jack to your audio system.

Boot the Raspberry Pi

Boot time is around 17 seconds

Tunes should start automatically playing

Close the switch to advance tracks
