def perf_note(pnotes, coeff):
    for note_name, coeff_min, coeff_max in pnotes:
        if coeff_min <= coeff <= coeff_max:
            return note_name
    return "Unknown note" 
if __name__ == "__main__":
    pnotes = [['head note', 1, 14],
              ['heart note', 15, 60],
              ['base note', 61, 100]]

    note = perf_note(pnotes, 8)
    print(note)  

    note = perf_note(pnotes, 34)
    print(note) 

    note = perf_note(pnotes, 78)
    print(note) 
