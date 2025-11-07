def cam_expos(neutral, photographer):
    """
    Calculates the difference in camera exposure settings.
    """
    f_stops = ['f/1.4', 'f/2', 'f/2.8', 'f/4', 'f/5.6', 'f/8', 'f/11', 'f/16', 'f/22']
    shutter_speeds = ['1/4', '1/8', '1/15', '1/30', '1/60', '1/125', '1/250', '1/500', '1/1000', '1/2000', '1/4000']
    isos = [100, 200, 400, 800, 1600, 3200]
    
    # F-stops: A larger f-stop number (higher index) means less exposure.
    # The difference is (neutral_index - photographer_index).
    diff_f = f_stops.index(neutral[0]) - f_stops.index(photographer[0])
    
    # Shutter speeds: A faster shutter speed (higher index) means less exposure.
    # The difference is (neutral_index - photographer_index).
    diff_shutter = shutter_speeds.index(neutral[1]) - shutter_speeds.index(photographer[1])
    
    # ISO: A higher ISO number (higher index) means more exposure.
    # The difference is (photographer_index - neutral_index).
    diff_iso = isos.index(int(photographer[2])) - isos.index(int(neutral[2]))
    
    # The total difference is the sum of all three.
    total_diff = diff_f + diff_shutter + diff_iso
    
    return (diff_f, diff_shutter, diff_iso, total_diff)

if __name__ == '__main__':
    # Invocation example 1
    res = cam_expos(['f/2.8', '1/500', '400'], ['f/5.6', '1/125', '200'])
    print(res)

    # Invocation example 2
    res = cam_expos(['f/2.8', '1/500', '400'], ['f/1.4', '1/60', '100'])
    print(res)