# AtariSTSongPlayer
Endless Atari ST Chip Tune player for install in car.

Run Raspberry Pi OS on a Pi 3 Model A+.

Install build tools:
sudo apt-get install cmake g++ libao-dev xxd libasound2-dev

Download and compile PSG play from https://github.com/frno7/psgplay with:
git clone --recurse-submodules https://github.com/frno7/psgplay.git
cd psgplay/
make ALSA=1 psgplay

Download the SNDH Atari ST YM2149 archive from https://sndh.atari.org/
Extract it to /home/pi/music

Place psgplay_start.sh from this repo in
/home/pi/psgplay_start.sh

Set it as executable
chmod +x psgplay_start.sh

Set the script up as a service to run at boot:
create /etc/systemd/system/psgplay.service as below:

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

Wire up a switch between GPIO 26 (pin 37) and GND (pin 39) on your Raspberry Pi

Connect the 3.5mm audio jack to your audio system.
Boot the Raspberry Pi
Tunes should start automatically playing
Close the switch to advance tracks
