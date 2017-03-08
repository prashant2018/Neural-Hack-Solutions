import os
import numpy as np

filename1 = "song1.mp3"
filename2 = "song2.mp3"
song1 = np.fromfile(filename1)
song2 = np.fromfile(filename2)
l1 = len(song1)
l2 = len(song2)
npsong = np.concatenate((song1[:l1/2],song2[l2/2:]))
npsong.tofile('song_r.mp3')