import oscillators, notes

pad_idx = 0

touching = False
just_touched = False
just_released = False




def output(time):
    if not touching:
        return 0.0

    note = notes.semitone_to_Hz(pad_idx, -1)
    return oscillators.saw(0.8, note, time)