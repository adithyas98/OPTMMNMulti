#!/usr/bin/env python3
#Created by Adithya Shastry
#Email: ams2590@columbia.edu
from scipy.io.wavfile import write 
import numpy as np
import os

class ToneGeneration:
    '''
    This class will serve as a way to generate tones
    '''
    def __init__(self,directory=None):
        '''
        Initialize the tone generation class
        Inputs:
            -directory: The directory to store the wav files
        '''
        self.directory = directory
    def generateWaveFile(self,duration,frequency,volume):
        '''
        Will take in inputs for multiple channels of the audio file and
        produce the audio file with sine waves
        Inputs:
            -duration:  (tuple)the duration (sec) of the tone generated
            -frequency: (tuple)the pitch (Hz) of the tone generated
            -volume: (tupel)the volume (dB) of the tone generated
        *Note all of the tuples must match in length
        Output:
            -The wave file of the tone generated will be stored in the directory
            with the following name format. 
            duration_{{Duration in Seconds}}_frequency_{{frequency in Hz}}_volume_{{volume in dB}}
        '''
        #Create an assert to make sure the tuples are of the same length
        assert len(duration) == len(frequency) and len(frequency) == len(volume)
        data = list()
        samplerate = 44100 
        for i in range(len(duration)):
            fs = frequency[i]
            d = duration[i]
            t = np.linspace(0., 1., samplerate*d)

            amplitude = volume[i] * np.iinfo(np.int16).max 

            data.append(amplitude * np.sin(2. * np.pi * fs * t))
        data = np.array(data).transpose()
        if self.directory != None:
            os.chdir(self.directory)
        write("duration{}frequency{}volume{}.wav".format(duration,frequency,volume), samplerate, data.astype(np.int16))
        return None


if __name__ == '__main__':
   TG = ToneGeneration(directory='/Users/adish/Documents/NYPSI and NKI Research/OptmmnMultiDeviantToneGeneration/tones')     
   duration = (1,)
   frequency = (200,)
   volume = (0.5,)
   TG.generateWaveFile(duration,frequency,volume)
