"""
Write a function named fire.
The function takes 2 filenames:
one is for covalence bond energies and
another is for the reaction specifying amounts of reactant
and product bonds.
The function reads both files for necessary information,
then calculates activation energy, releasing energy,
and the different energy
and appends the result at the end of the second file
---the reaction-bond file.
"""

def fire(fbond, fcombust):

    bond_energy = {}
    with open(fbond, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                bond, energy = parts
                bond_energy[bond] = float(energy)


    with open(fcombust, 'r+') as f:
        f.readline()  


        reactant = f.readline()
        if reactant[-1] == '\n':
            reactant = reactant[:-1]

        reactant = reactant.split('+')
        E1 = 0
        for b in reactant:
            pair = b.strip()
            num_bonds, bond_symbol = pair.split()
            bond_symbol = bond_symbol.strip()
            
            energy = bond_energy.get(bond_symbol, 0)
            E1 += energy * float(num_bonds)


        product = f.readline()
        if product[-1] == '\n':
            product = product[:-1]

        product = product.split('+')
        E2 = 0
        for b in product:
            pair = b.strip()
            num_bonds, bond_symbol = pair.split()
            bond_symbol = bond_symbol.strip()
            
            energy = bond_energy.get(bond_symbol, 0)
            E2 += energy * float(num_bonds)

        total_E = E1 - E2
        msg = '\nEa = {:,.1f} kJ, Er = {:,.1f} kJ, E = {:,.1f} kJ'.format(E1, E2, total_E)
        
        f.write(msg) 

if __name__ == '__main__':
    fire('bond_energy.txt', 'methane1.txt')