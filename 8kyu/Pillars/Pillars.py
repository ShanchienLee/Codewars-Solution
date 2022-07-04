def pillars(num_pill, dist, width):  
    if num_pill >= 2:
        return((num_pill - 1) * dist * 100 + (num_pill - 2) * width)
    elif num_pill == 1:
        return 0
