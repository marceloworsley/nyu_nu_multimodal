#!/bin/bash

export LD_LIBRARY_PATH="/home/respeaker/code/SSI/mobileSSI/bin_cmake/Linux/"
cd /home/respeaker/code/SSI/mobileSSI
./bin_cmake/Linux/xmlpipe ./recordingAudio/audio_write.pipeline
