def has_duplicates(lst):
    """Takes list and checks
    for duplicates

    lst: list
    returns: True if duplicates
    are present, False otherwise
    """
    dup = lst[:]
    dup.sort()
    for i in range(len(dup) - 1):
        if dup[i] == dup[i+1]:
            print("true")
            return True
    print("false")
    return False
