"""
Given a reaction of burning gas methane (CH4) in air: 
CH4 + 2 O2 --> CO2 + 2 H2O and the fact that 
when either CH4 or O2 runs out first the reaction stops and the other is left over. 
Write a function, named "ch4combus", to take in weights (in gram) of  CH4 and O2 and 
reports what will be left after the burning.
Note: 
    molar mass M = mass (in kg) of 1 mole of the substance;
    1 mole = 6.02214076×10^23 particles (e.g., molecules, atoms, ions, electrons, etc.).
    molar mass of water = 18.015 g/mol
    atomic weight: 
        H ~ 1.008 g/mol; C ~ 12.011 g/mol; O ~ 15.999 g/mol
	https://en.wikibooks.org/wiki/General_Chemistry/Energy_changes_in_chemical_reactions
"""

# Write your function here

def ch4combus(ch4_g, o2_g):
    # (1) Molecular weights (g/mol)
    mw_ch4 = 12.011 + 1.008 * 4     # 16.043
    mw_o2 = 15.999 * 2              # 31.998
    mw_co2 = 12.011 + 15.999 * 2    # 44.009
    mw_h2o = 1.008 * 2 + 15.999     # 18.015

    # (2) Moles
    mol_ch4 = ch4_g / mw_ch4
    mol_o2 = o2_g / mw_o2

    # (3) Determine limiting reactant
    if mol_ch4 <= mol_o2 / 2:
        # CH4 is limiting
        used_ch4_g = ch4_g
        used_o2_g = mol_ch4 * 2 * mw_o2
        left_ch4 = 0.00
        left_o2 = o2_g - used_o2_g
        mol_co2 = mol_ch4
        mol_h2o = mol_ch4 * 2
    else:
        # O2 is limiting
        used_o2_g = o2_g
        used_ch4_g = (mol_o2 / 2) * mw_ch4
        left_ch4 = ch4_g - used_ch4_g
        left_o2 = 0.00
        mol_co2 = mol_o2 / 2
        mol_h2o = mol_co2 * 2

    # (4) Product weight
    product_weight = used_ch4_g + used_o2_g

    # (5) Proportion
    total_product_ratio = (mol_co2 * mw_co2) + (mol_h2o * mw_h2o)
    co2_g = (mol_co2 * mw_co2) / total_product_ratio * product_weight
    h2o_g = (mol_h2o * mw_h2o) / total_product_ratio * product_weight

    return (left_ch4, left_o2, co2_g, h2o_g)

# Do not edit below this line.
# ==============================================================

if __name__ == '__main__':
    m = input('Methane (CH4, in g):')
    o = input('Oxygen (O2, in g):')
    print('CH4: %.2f g. O2 %.2f g. CO2 %.2f g. H2O %.2f g'%
        ch4combus(float(m), float(o)))
