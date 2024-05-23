import serial_IO, soundplayer, notes
import synthesizer
from time import time, sleep

for port in serial_IO.get_comports():
    print(port)

comport = int(input(">>> COM"))
serial_IO.open_comport(comport)

soundplayer.start()

#wait for the styloino to get ready
while not serial_IO.is_ready():
    sleep(0.1)

print("styloino: ok")
print("output latency:", round(soundplayer.get_latency(), 2), "ms")
print("ready")

serial_IO.set_buzzer(False)

delta = 0.1

pad_idx = 0
#the readings when changing move gradually to the correct value, 
#normally causing the computer tho think the note has changed multiple times
#this variable keeps track of recent changes so the computer can reject changes by ignoring changes right after a first detected change
change_ignore_time = 0
change_ignore = 0.1 #in seconds

while True:
    start_time = time()
    reading = serial_IO.get_reading()

    if reading == None:
        print("missed serial packet")
        continue

    stylus0 = serial_IO.get_stylus_data(reading, 0)

    change_ignore_time = max(change_ignore_time-delta, 0)
    
    prev_pad_idx = pad_idx
    pad_idx = stylus0[1]

    synthesizer.pad_idx = pad_idx
    synthesizer.touching = stylus0[0]


    if (pad_idx != 0 and prev_pad_idx == 0 ) and change_ignore_time == 0:
        change_ignore_time += change_ignore

    delta = time() - start_time



soundplayer.stop()