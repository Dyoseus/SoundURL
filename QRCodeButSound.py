#START OF PLAYING AUDIO
import pyaudio
import struct
import math
import string

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

def data_for_freq(frequency: float, time: float = None):

    frame_count = int(RATE * time)

    remainder_frames = frame_count % RATE
    wavedata = []

    for i in range(frame_count):
        a = RATE / frequency
        b = i / a

        c = b * (2 * math.pi)
        d = math.sin(c) * 32767
        e = int(d)
        wavedata.append(e)

    for i in range(remainder_frames):
        wavedata.append(0)

    number_of_bytes = str(len(wavedata))  
    wavedata = struct.pack(number_of_bytes + 'h', *wavedata)

    return wavedata


def play(frequency: float, time: float):

    frames = data_for_freq(frequency/2, time)
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)
    stream.write(frames)
    stream.stop_stream()
    stream.close()

#play is the function. frequencyvalue and duration determine how long/what the freq played is.
#END OF PLAYSOUND

ascii_char = string.printable
freq = list(range(230, 4231, 40))
zipped = dict(zip(ascii_char, freq))
starting_freq = 9000
ending_freq = 9000
duration = 0.5
word = input("Enter a URL:")
wordList = list(word)
startplay = input("hit enter to begin broadcast")
play(starting_freq, duration)
for i in range(len(word)): 
    play(zipped[word[i]], duration)
play(ending_freq, duration)