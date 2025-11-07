"""
P4. Also, inspired by film The Martian 2015. 
Write function named martian_botanist. The function takes a number of sols 
(sort of Martian days, as integer), daily potato consumption (in kg, as float), 
and estimated potato production per area (in kg/m², as float), then calculates 
the planting area (in m², as float) to produce sufficient food to survive 
Martian living till the rescue arrives.

Hint: total potato needed (in kg) = number of sols × daily consumption (in kg);
planting area (in m²) = total potato needed (in kg) / production (in kg/m²).
"""

def martian_botanist(sols, daily_consumption_kg, production_per_m2):
   
    total_potato_needed_kg = sols * daily_consumption_kg
    
    planting_area_m2 = total_potato_needed_kg / production_per_m2
    
    return planting_area_m2

if __name__ == '__main__':
    area = martian_botanist(150, 2, 2.4)
    print('planting area:', area, 'sq. m.')
    area = martian_botanist(900, 2.5, 1.2)
    print('planting area:', area, 'sq. m.')
    area = martian_botanist(200, 2.4, 1.6)
    print('planting area:', area, 'sq. m.')