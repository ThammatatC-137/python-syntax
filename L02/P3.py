def survive_mars(area, depth):
    depth_m = depth / 100.0  
    volume = area * depth_m  
    water = volume * 40      
    return water

if __name__ == '__main__':
    w = survive_mars(126, 30)
    print('water', w, 'L')
    
    w = survive_mars(150, 40)
    print('water', w, 'L')
    
    w = survive_mars(100, 35)
    print('water', w, 'L')
