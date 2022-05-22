def chop(t):
    """Takes list, removes first and
    last elements

    t: list of elements
    returns: None
    """
    for i in range(len(t)):
        if i == 0 or i == len(t) -1:
            del(t[i])
    print(t)
    return t

t = [1, 2, 3, 4]
chop(t)
