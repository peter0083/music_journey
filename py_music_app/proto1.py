
from turtle import *
import vlc
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile

# spectrogram generator
# Fs, aud = wavfile.read("../music_app/src/audio/Flower_Sample.wav")
# # select left channel only
# aud = aud[:,0]
# # trim the first 125 seconds
# first = aud[:int(Fs*125)]
# powerSpectrum, frequenciesFound, time, imageAxis = plt.specgram(first, Fs=Fs)
# plt.show()


player = vlc.MediaPlayer("../music_app/src/audio/Flower_Sample.mp3")

speed("slow")
  
# turning the turtle to face upwards
rt(-90)
  
# the acute angle between
# the base and branch of the Y
angle = 30
  
# function to plot a Y
def y(sz, level):   
  
    if level > 0:
        colormode(255)
          
        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        pencolor(0, 255//level, 0)
          
        # drawing the base
        fd(sz)
  
        rt(angle)
  
        # recursive call for
        # the right subtree
        y(0.8 * sz, level-1)
          
        pencolor(0, 255//level, 0)
          
        lt( 2 * angle )
  
        # recursive call for
        # the left subtree
        y(0.8 * sz, level-1)
          
        pencolor(0, 255//level, 0)
          
        rt(angle)
        fd(-sz)
           
          
player.play()
# tree of size 80 and level 7
y(80, 7)