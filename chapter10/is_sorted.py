def is_sorted(lst):
    """Takes list and checks if sorted
    in ascending order

    lst: list
    returns: True if sorted, False otherwise
    """
    if lst == sorted(lst):
        print("true")
        return True
    else:
        print("false")
        return False

is_sorted([1, 2, 2])

is_sorted(['b', 'a'])
