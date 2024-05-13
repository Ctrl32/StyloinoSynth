
def semitone_to_Hz(semitone:int, octave:int):
  freq = 440.0 * 2**((semitone+12.0*octave)/12.0)
  return freq