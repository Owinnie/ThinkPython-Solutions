def middle(li):
    """Gets the middle elements of
    a list

    li: list of elements

    returns: new list with only middle
    elements
    """
    print([li[i] for i in range(1, len(li)-1)])
    return [li[i] for i in range(1, len(li)-1)]

t = [1, 2, 3, 4]
middle(t)
