#!/bin/bash

cd /home/pi/code/SSI/mobileSSI
python3 stopRecording.py
sleep 5
now=$(date +"%Y_%m_%d_%H_%M_%S")
sudo mkdir /var/www/html/files/$now
sudo cp recordRaspicam/video.mp4 /var/www/html/files/$now/
sudo ssh respeaker@192.168.50.150 '/home/respeaker/code/SSI/mobileSSI/recordingAudio/produceWav.sh'
sudo scp respeaker@192.168.50.150:/home/respeaker/code/SSI/mobileSSI/recordingAudio/audio.wav /var/www/html/files/$now/audio.wav


