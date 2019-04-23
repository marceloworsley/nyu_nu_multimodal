#!/bin/bash

cd /home/respeaker/code/SSI/mobileSSI/recordingAudio
rm audio.raw
mv audio.stream~ audio.raw
sox -r 16000 -e float -b 32 -c 6 audio.raw audio.wav

