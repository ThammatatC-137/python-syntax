def krill_consumption(feeding, whales):
    """
    Estimates the total daily krill consumption.
    """
    total_consumption = 0
 
    for whale_type, count in whales.items():

        if whale_type in feeding:

            total_consumption += feeding[whale_type] * count

    return total_consumption

if __name__ == '__main__':
    # Invocation example 1
    feeding = {'Humpback whale': 2000, 'Gray whale': 1500, 'Bowhead whale': 2500, 'Blue whale': 3600}
    whales = {'Humpback whale': 8, 'Gray whale': 3, 'Bowhead whale': 1, 'Blue whale': 12}
    total_consum = krill_consumption(feeding, whales)
    print('Estimate daily consumption: %d kg of krill' % total_consum)
    
    # Invocation example 2
    whales = {'Humpback whale': 8, 'Gray whale': 3}
    total_consum = krill_consumption(feeding, whales)
    print('Estimate daily consumption: %d kg of krill' % total_consum)
    
    # Invocation example 3
    whales = {'Bowhead whale': 80000}
    total_consum = krill_consumption(feeding, whales)
    print('Estimate daily consumption: %d kg of krill' % total_consum)