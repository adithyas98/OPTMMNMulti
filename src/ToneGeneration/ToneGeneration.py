#!/usr/bin/env python3
#Created by Adithya Shastry
#Email: ams2590@columbia.edu
from scipy.io.wavfile import write 
import numpy as np



if __name__ == '__main__':
    samplerate = 44100; fs = 400
    duration = 3
    t = np.linspace(0., 1, samplerate*duration)

    amplitude = np.iinfo(np.int16).max

    data = amplitude * np.sin(2. * np.pi * fs * t)

    write("example{}_{}.wav".format(fs,duration), samplerate, data.astype(np.int16))
