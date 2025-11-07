import random

BOARD_SIZE = 8
NUM_QUEENS = 5
NUM_BISHOPS = 5

# ====== Helper Functions ======
def queen_attacks(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2
    return r1 == r2 or c1 == c2 or abs(r1-r2) == abs(c1-c2)

def bishop_attacks(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2
    return abs(r1-r2) == abs(c1-c2)

def compute_conflicts(queens, bishops):
    conflicts = 0
    # Queen vs Queen
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            if queen_attacks(queens[i], queens[j]):
                conflicts += 1
    # Bishop vs Bishop
    for i in range(len(bishops)):
        for j in range(i+1, len(bishops)):
            if bishop_attacks(bishops[i], bishops[j]):
                conflicts += 1
    # Queen vs Bishop
    for q in queens:
        for b in bishops:
            if queen_attacks(q, b) or bishop_attacks(q, b):
                conflicts += 1
    return conflicts

def random_board():
    positions = set()
    queens = []
    bishops = []
    while len(queens) < NUM_QUEENS:
        pos = (random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
        if pos not in positions:
            queens.append(pos)
            positions.add(pos)
    while len(bishops) < NUM_BISHOPS:
        pos = (random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
        if pos not in positions:
            bishops.append(pos)
            positions.add(pos)
    return queens, bishops

def print_board(queens, bishops):
    for r in range(BOARD_SIZE):
        row = ""
        for c in range(BOARD_SIZE):
            if (r,c) in queens:
                row += "Q "
            elif (r,c) in bishops:
                row += "B "
            else:
                row += ". "
        print(row)
    print()

# ====== Hill Climbing Algorithm ======
def hill_climb_mixed(max_steps=1000):
    queens, bishops = random_board()
    current_conflicts = compute_conflicts(queens, bishops)

    for step in range(max_steps):
        if current_conflicts == 0:
            return queens, bishops, step
        
        neighbors = []
        # Move Queens
        for i in range(len(queens)):
            for r in range(BOARD_SIZE):
                for c in range(BOARD_SIZE):
                    if (r,c) not in queens and (r,c) not in bishops:
                        new_queens = queens[:]
                        new_queens[i] = (r,c)
                        new_conflicts = compute_conflicts(new_queens, bishops)
                        if new_conflicts < current_conflicts:
                            neighbors.append((new_queens, bishops, new_conflicts))
        # Move Bishops
        for i in range(len(bishops)):
            for r in range(BOARD_SIZE):
                for c in range(BOARD_SIZE):
                    if (r,c) not in queens and (r,c) not in bishops:
                        new_bishops = bishops[:]
                        new_bishops[i] = (r,c)
                        new_conflicts = compute_conflicts(queens, new_bishops)
                        if new_conflicts < current_conflicts:
                            neighbors.append((queens, new_bishops, new_conflicts))
        
        if not neighbors:
            return queens, bishops, step  # local minima

        queens, bishops, current_conflicts = random.choice(neighbors)

    return queens, bishops, max_steps

# ====== Run Example ======
queens, bishops, steps = hill_climb_mixed()
print(f"Solved in {steps} steps")
print_board(queens, bishops)
