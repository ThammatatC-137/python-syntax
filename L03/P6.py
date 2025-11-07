def rational_decision(info_table, person):
    """
    Determines the rational decision based on a Prisoner's Dilemma payoff table.
    0 means 'not confess', 1 means 'confess', None means 'no independently rational choice'.
    """
    # Payoff for the person
    # info_table[person][row][col]
    # row 0 = not confess, row 1 = confess
    # col 0 = other not confess, col 1 = other confess

    # Payoff if the person chooses 'not confess'
    not_confess_if_other_not_confess = info_table[person][0][0]
    not_confess_if_other_confess = info_table[person][0][1]

    # Payoff if the person chooses 'confess'
    confess_if_other_not_confess = info_table[person][1][0]
    confess_if_other_confess = info_table[person][1][1]

    # Check if 'confess' is the dominant strategy
    # Confess is better than not confess, regardless of what the other player does.
    if confess_if_other_not_confess < not_confess_if_other_not_confess and \
       confess_if_other_confess < not_confess_if_other_confess:
        return 1  # 1 corresponds to 'confess'

    # Check if 'not confess' is the dominant strategy
    # Not confess is better than confess, regardless of what the other player does.
    if not_confess_if_other_not_confess < confess_if_other_not_confess and \
       not_confess_if_other_confess < confess_if_other_confess:
        return 0  # 0 corresponds to 'not confess'

    # If neither is the dominant strategy
    return None  # No independently rational choice

if __name__ == '__main__':
    choices = ['not confess', 'confess', 'no independently rational choice']
    s = {'Lobha': [[3, 10], [1, 5]], 'Raga': [[3, 10], [1, 5]]}
    p = 'Lobha'
    r = rational_decision(s, p)
    if r is None:
        print(p, ':', choices[2])
    else:
        print(p, ':', choices[r])