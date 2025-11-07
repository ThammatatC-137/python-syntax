

def simple_poet(filename):

    with open(filename, 'r') as f:
        lines = f.readlines()
        
    processed_lines = [line.strip('\n') for line in lines]
    
    return processed_lines

if __name__ == '__main__':

    try:
        with open('poem.txt', 'w') as f:
            f.write("Where the departed goes, by Student\n")
            f.write("\n")
            f.write("Where herons go\n")
            f.write("is a place for a departed soul.\n")
            f.write("What the choirs say\n")
            f.write("is how soul not just go away.\n")
            f.write("Like an origami,\n")
            f.write("it just shifts to a new story.\n")
            f.write("Transform the end of an old\n")
            f.write("to the beginning of a new fold.")
    except Exception as e:
        print("Error creating dummy file: {}".format(e))
        
    res = simple_poet('poem.txt')
    print(res)