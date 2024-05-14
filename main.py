import serial_IO, soundplayer, notes

for port in serial_IO.get_comports():
    print(port)

comport = int(input(">>> COM"))
serial_IO.open_comport(comport)

soundplayer.start()

#wait for the styloino to get ready
while not serial_IO.is_ready():
    pass

print("styloino: ok")
print("output latency:", round(soundplayer.get_latency(), 2), "ms")
print("ready")

serial_IO.set_buzzer(False)

note = 0

while True:
    reading = serial_IO.get_reading()

    if reading == None:
        print("missed serial packet")
        continue

    stylus0 = serial_IO.get_stylus_data(reading, 0)

    if stylus0[0] == False:
        soundplayer.set_oscillator(0, 1)
        note = None
        continue
    

    prev_note = note
    note = stylus0[1]-12

    if note != prev_note:
        frequency = notes.semitone_to_Hz(note, -1)
        soundplayer.set_oscillator(0.8, frequency)


soundplayer.stop()