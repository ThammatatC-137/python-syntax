def star_lagtime(light_speed, name, distance_km):
    distance_m = distance_km * 1000
    time_sec = distance_m / light_speed
    print(name)
    return time_sec

if __name__ == '__main__':
    t = star_lagtime(299792458, "sun", 149600000)
    print(t)
    print(format(t, ".2f") + " s = " + format(t/60, ".2f") + " min.")
