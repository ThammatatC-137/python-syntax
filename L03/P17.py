def carbon_14_dating():
    
    half_life = 5730
    
    ratio_input = input("ratio: ")
    sensitivity_input = input("sensitivity: ")
    
    try:
        initial_ratio = int(ratio_input)
    except ValueError:
        initial_ratio = float(ratio_input)
    
    sensitivity = float(sensitivity_input)
    
    year = 0
    
    print("Year {}: ratio = {}".format(year, initial_ratio))
    
    current_ratio = float(initial_ratio)
    current_ratio /= 2
    year += half_life
    
    while current_ratio >= sensitivity:
        print("Year {}: ratio = {}".format(year, current_ratio))
        current_ratio /= 2
        year += half_life

if __name__ == '__main__':
    carbon_14_dating()