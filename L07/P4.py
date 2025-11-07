from collections import deque

def P4_crossriver(initial):
    # initial = (missionaries_wait, cannibals_wait, missionaries_crossed, cannibals_crossed, boat_on_waiting)
    # action = (missionaries_in_boat, cannibals_in_boat)
    actions = [(1,0), (0,1), (1,1), (2,0), (0,2)]
    
    visited = set()
    queue = deque()
    # store path of actions taken
    queue.append( (initial, []) )
    
    while queue:
        state, path = queue.popleft()
        mw, cw, mc, cc, boat = state
        
        # goal check
        if mw == 0 and cw == 0:
            return path
        
        for m, c in actions:
            # valid move: at least 1, at most 2
            if m + c >= 1 and m + c <= 2:
                if boat == 1:  # boat on waiting bank
                    new_mw = mw - m
                    new_cw = cw - c
                    new_mc = mc + m
                    new_cc = cc + c
                    new_boat = 0
                else:  # boat on crossed side
                    new_mw = mw + m
                    new_cw = cw + c
                    new_mc = mc - m
                    new_cc = cc - c
                    new_boat = 1
                
                # check valid numbers
                if new_mw < 0 or new_cw < 0 or new_mc < 0 or new_cc < 0:
                    continue
                # missionaries never outnumbered
                if (new_mw > 0 and new_mw < new_cw) or (new_mc > 0 and new_mc < new_cc):
                    continue
                
                new_state = (new_mw, new_cw, new_mc, new_cc, new_boat)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append( (new_state, path + [(m,c)]) )
    
    return []  # no solution found

if __name__ == "__main__":
    # ตัวอย่างรัน
    result = P4_crossriver((2,2,1,1,1))
    print(result)
