
def calculate_landfill_size():

    population = 70000000
    days_in_year = 365
    sqm_per_rai = 1600

    waste_per_person_input = input("Waste: ")
    holding_capacity_input = input("Cap: ")
    
    waste_per_person = float(waste_per_person_input)
    holding_capacity = float(holding_capacity_input)

    total_daily_waste = waste_per_person * population

    land_size_sqm_daily = total_daily_waste / holding_capacity

    land_size_rai_daily = land_size_sqm_daily / sqm_per_rai

    annual_waste = total_daily_waste * days_in_year
    land_size_sqm_annual = annual_waste / holding_capacity
    land_size_rai_annual = land_size_sqm_annual / sqm_per_rai

    print("Total waste= {:.2f}".format(total_daily_waste))
    print("Landfill= {:.2f}".format(land_size_rai_daily))
    print("Annual land= {:.2f}".format(land_size_rai_annual))

if __name__ == '__main__':
    calculate_landfill_size()