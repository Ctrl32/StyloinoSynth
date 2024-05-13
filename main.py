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
        continue
    

    note = stylus0[1]-12

    frequency = notes.semitone_to_Hz(note, -1)
    soundplayer.set_oscillator(0.8, frequency)


soundplayer.stop()
            



# root = tk.Tk()
# root.title("Styloino Studio")

# menu = tk.Menu(root)
# root.config(menu=menu)

# comport_menu = tk.Menu(menu, tearoff=False)
# comports = serial_receiver.get_comports()   
# for port in comports:
#     comport_menu.add_command(label=str(port))

# menu.add_cascade(label="COM", menu=comport_menu)



# root.mainloop()