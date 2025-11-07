import math

def Hipparchus(do, th_m):

    Dm = (do / 2) / math.tan(math.radians(90 - th_m))

    D_off1 = (do / 2) / math.tan(math.radians(90 - (th_m - 0.01)))
    D_off2 = (do / 2) / math.tan(math.radians(90 - (th_m + 0.01)))
    
    return (Dm, min(D_off1, D_off2), max(D_off1, D_off2))

def Aristarchus(dm, th_s):
    
    Ds = dm / math.tan(math.radians(th_s))

    
    D_off1 = dm / math.tan(math.radians(th_s - 0.01))
    D_off2 = dm / math.tan(math.radians(th_s + 0.01))
    
    # Return the values as a tuple, with the range sorted
    return (Ds, min(D_off1, D_off2), max(D_off1, D_off2))


if __name__ == '__main__':
    # Invocation example 1
    res = Hipparchus(400, 89.97)
    print('Hipparchus: {:,.2f} km; [{:,.0f} , {:,.0f}] if 0.01 deg off'.format(*res))
    
    # Invocation example 2
    res = Aristarchus(381972, 0.15)
    print('Aristarchus: {:,.2f} km; [{:,.0f} , {:,.0f}] if 0.01 deg off'.format(*res))