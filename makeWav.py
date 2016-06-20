# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:44:45 2016

@author: Oliver
"""
import wave, numpy, struct, time
from winsound import PlaySound as play
from winsound import SND_FILENAME as wav

print("Create file using wave, storing frames in an array and using writeframes only once")

def timing(ref):
    if ref == 1:
        global start 
        start = time.time()
        
    if ref == 2:
        end = time.time()
        print(end-start)

class Sound(object):
    
    #perhaps make channels and samplewidth modifiable via __init__ 
    samples = []
    def __init__(self, sr=None, dur=None, name=None, channels = None, sampleWidth = None):

        if sr is None:
            self.sr = 44100
        else:
            self.sr = sr
        
        if dur is None:
            self.dur = 2
        else:
            self.dur = dur
        
        self.sampleLength = self.sr * self.dur
        
        if name is None:
            self.name = 'noise.wav'
        else:
            self.name = name
            
        if channels is None:
            self.channels = 2
        else:
            self.channels = channels
        
        if sampleWidth is None:
            self.sampleWidth = 2
        else:
            self.sampleWidth = sampleWidth

        
        self.noise_output = wave.open(self.name, 'w')
        self.noise_output.setparams((self.channels, self.sampleWidth, self.sr, 0, 'NONE', 'not compressed'))    
      
    #Populate .wav file with random values
    def white(self):
        self.samples = []
        for i in range(0, self.sampleLength):
        	value = numpy.random.randint(-32767, 32767)
        	packed_value = struct.pack('h', value)
        	self.samples.append(packed_value)
#        	values.append(packed_value)
         
        self.writeWav()
         
    def sinusoid(self, freq):
        self.samples = []
        samplesInCycle = 1.0 / freq * self.sr
        sineList = numpy.sin(numpy.linspace(0, 2 * numpy.pi, samplesInCycle, dtype = 'h'))
        sineList = numpy.ndarray.tolist(sineList)
        steps = self.sampleLength // samplesInCycle
        for i in range(int(steps)):
            self.samples.append(sineList)
        
        self.writeWav()
        
    def writeWav(self):
            value_str = b''.join(str(v) for v in self.samples)
            self.noise_output.writeframes(value_str)
            self.noise_output.close()

s1 = Sound(dur = 3)
s1.sinusoid(100)

play('noise.wav', wav)

