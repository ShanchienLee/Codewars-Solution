def enough(cap, on, wait):
    available = cap - on - wait
    if available >= 0:
        return 0
    else:
        return -available
