# import pyaudio
# import numpy as np
# import oscillators
# import gb

# sample_rate = 44100
# curr_time = 0

# amplitude  = 0
# frequency = 1

# p = pyaudio.PyAudio()
# stream = None


# def callback(in_data, frame_count, time_info, status):
#     global curr_time
#     chunk = np.zeros(frame_count, dtype=np.float32)
#     for i in range(frame_count):
#         time = curr_time/sample_rate
#         chunk[i] = (oscillators.saw(amplitude, frequency, time) + oscillators.sin(amplitude, frequency, time))/2

#         curr_time += 1


#     chunk = chunk.tobytes()
#     return (chunk, pyaudio.paContinue)

# def start():
#     global stream
#     stream = p.open(format=pyaudio.paFloat32, channels=1, rate=sample_rate, output=True, stream_callback=callback, frames_per_buffer=gb.CHUNK_SIZE)

# def get_latency():
#     return stream.get_output_latency()*1000

    
# def set_oscillator(amp, freq):
#     global amplitude, frequency
#     amplitude = amp
#     frequency = freq

# def stop():
#     stream.close()
#     p.terminate()


import sounddevice as sd
import numpy as np
import oscillators
import time

sample_rate = 44100
start_idx = 0
curr_time = 0

amplitude = 0.5
frequency = 440

chunk_size = 1024

def callback(outdata, frames, time, status):
    global curr_time
    chunk = np.zeros(frames, dtype=np.float32)
    for i in range(frames):
        time = curr_time/sample_rate
        chunk[i] = oscillators.sin(amplitude, frequency, time)
        curr_time += 1

    chunk = chunk.reshape(-1, 1)
    outdata[:] = chunk



stream = sd.OutputStream(channels=1, callback=callback, samplerate=sample_rate, blocksize=chunk_size, latency=0.01)
stream.start()

time.sleep(1)
