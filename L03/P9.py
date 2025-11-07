"""
Write a function named sweet to take 2 filenames:
one is for a sweetness table and
another one is for sweeteners in a drink.
The function calculates estimated sweetness of the drink
comparable to 10% sucrose solution,
and appends its calculate to the end of the second file
---the drink-sweetener file.
"""

def sweet(fsweet, fdrink):

    # 1. Retrieve sweetness dict from fsweet file
    sweetness = {}
    with open(fsweet, 'r') as f:
        # Skip the header line
        f.readline()
        for line in f:
            parts = line.strip().split()
            # Check if the line has at least 2 parts (substance and sweetness)
            if len(parts) >= 2:
                substance = parts[0]
                # Convert sweetness value from string to float
                sweetness_level = float(parts[1])
                sweetness[substance] = sweetness_level
    
    # 2. Calculate the estimated sweetness from fdrink file
    sweet_sum = 0
    with open(fdrink, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and lines that are not part of the ingredients list
            # We assume ingredient lines have exactly 2 parts
            parts = line.split()
            if len(parts) == 2:
                substance = parts[0]
                # Convert weight from string to float
                weight = float(parts[1])
                
                # Add the weighted sweetness to the total sum
                if substance in sweetness:
                    sweet_sum += weight * sweetness[substance]

    # 3. Write/append message to the end of fdrink file
    msg = "\nSweet as {:.1f}% sucrose solution".format(sweet_sum)
    with open(fdrink, 'a') as f:
        f.write(msg)

if __name__ == '__main__':
    sweet('sweetness1.txt', 'CocaPanda.txt')