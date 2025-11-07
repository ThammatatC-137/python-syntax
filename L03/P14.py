
density = float(input("Fuel density (in kg/L): "))

calorific_value = float(input("Calorific value (in MJ/kg): "))

energy_per_liter = density * calorific_value

liters_per_bbl = 158.987
energy_per_bbl = energy_per_liter * liters_per_bbl

print("This fuel has energy per volume of {:.2f} MJ/L.".format(energy_per_liter))
print("That is {:.2f} MJ/bbl.".format(energy_per_bbl))