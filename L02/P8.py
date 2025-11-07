"""
Student's Name: !!!Thammatat Charoensook!!!
ID: !!!663040118-5!!!
Diatonic notes on scale.
Print all diatonic notes on scale, given the scale key.
"""

from P8_helper import print_scale # Keep this untouched

# Make the diatonic function work

def diatonic(scale_key):

    # step pattern ในสเกลเมเจอร์ (major scale)
    steps = [2, 2, 1, 2, 2, 2, 1]

    notes = [scale_key]  # โน้ตตัวแรกคือ scale_key เอง

    current_note = scale_key
    for i in range(6):  # สร้างโน้ตเพิ่มอีก 6 ตัว รวมเป็น 7 ตัว
        current_note += steps[i]
        if current_note > 12:
            current_note -= 12
        notes.append(current_note)

    return tuple(notes)

# Do not edit below this line.
# ------------------------------------------

if __name__ == "__main__":

    key_of = int(input('Enter the key [1-12]:'))
    k1, k2, k3, k4, k5, k6, k7 = diatonic(key_of)
    print_scale(k1, k2, k3, k4, k5, k6, k7)
    if key_of == 7:
        s = __doc__
        sname = s.split('P20')[0]
        print(sname)
