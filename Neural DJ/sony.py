import os
import numpy as np

filename1 = "song1.mp3"
filename2 = "song2.mp3"

song1 = open(filename1,"rb").readlines()
song2 = open(filename2,"rb").readlines()

song_fin = song1[len(song1)/2:] + song1[:len(song2)/2]
p = bytes(song_fin)
print p[:10]

f = open('songy.mp3',"wb")
f.write(p)
f.close()