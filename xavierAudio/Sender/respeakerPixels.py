from pixel_ring import pixel_ring
import mraa
import numpy as np
import time
import os

def getOptions(opts, vars):

    pass


def getEventAddress(opts, vars):
    return 'doa,doa@audio'


def consume_enter(sins, board, opts, vars):
    en = mraa.Gpio(12)
    if os.geteuid() != 0 :
        time.sleep(1)

    en.dir(mraa.DIR_OUT)
    en.write(0)
    vars["led"]=en
    pixel_ring.set_brightness(20)


def send_rate(pos, last_pos, sr, board, opts, vars):

    dist = pos - last_pos
    rate = 60.0 / (dist / sr)

    if rate >= opts['min_rate'] and rate <= opts['max_rate']:
        time = int(1000 * last_pos/sr)
        dur = int(1000 * dist/sr)
        board.update(time, dur, 'rate@ecg', float(rate))
        board.update(time+dur, 0, 'peak@ecg', float(pos))


def consume(info, sins, board, opts, vars):

    sr = sins[0].sr
    dim = sins[0].dim
    #x = np.asarray(sins[0])
    #pixel_ring.wakeup()
    position = 3

    pixels = [0, 0, 0, 0] * 12
    pixels[5] = 255
    pixels[8] = 100

    pixel_ring.show(pixels)
    #pixel_ring.think()
    #vars["led"].write(1)

def consume_flush(sins, board, opts, vars):
    pixel_ring.off()
    vars['led'].write(1)
