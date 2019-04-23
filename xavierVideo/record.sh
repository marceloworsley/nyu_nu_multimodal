#!/bin/bash

cd /home/pi/code/SSI/mobileSSI
raspivid -n -w 800 -h 640 -t 0 -fps 15 -l -o tcp://0.0.0.0:3333 &
sleep 1
export LD_LIBRARY_PATH="/home/pi/code/SSI/mobileSSI/bin_cmake/Linux/"
./bin_cmake/Linux/xmlpipe ./recordRaspicam/raspiffmpeg.pipeline & 
sudo ssh respeaker@192.168.50.150 '/home/respeaker/code/SSI/mobileSSI/recordingAudio/start_record.sh &' &
sleep 10
python3 startRecording.py
