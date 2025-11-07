import math

def earthquake(events):
    result = []
    for event in events:
        date_loc, M = event
        logE = 4.8 + 1.5 * M
        E = 10 ** logE
        result.append([date_loc, M, E])
    return result

if __name__ == "__main__":
    events = [['2019 02 22 Ecuador', 7.5],
              ['2018 08 19 Fiji', 8.2],
              ['2017 09 08 Mexico', 9.1]]
    res = earthquake(events)
    print(res)
