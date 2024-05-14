import sounddevice as sd
import numpy as np
import oscillators
import gb

sample_rate = 44100
start_idx = 0
curr_time = 0

amplitude = 0
frequency = 1

def callback(outdata, frames, time, status):
    global curr_time
    chunk = np.zeros(frames, dtype=np.float32)
    for i in range(frames):
        time = curr_time/sample_rate
        chunk[i] = oscillators.sin(amplitude, frequency, time)
        curr_time += 1

    chunk = chunk.reshape(-1, 1)
    outdata[:] = chunk


def start():
    global stream
    stream = sd.OutputStream(channels=1, callback=callback, samplerate=sample_rate, blocksize=gb.CHUNK_SIZE, latency=0.001)
    stream.start()

def get_latency():
    return stream.latency*1000

    
def set_oscillator(amp, freq):
    global amplitude, frequency
    amplitude = amp
    frequency = freq

def stop():
    stream.abort()
