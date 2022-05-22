def nested_sum(li):
    """Takes a list of lists of ints
    and sums up the elements

    li: a list of lists of ints
    
    returns: sum total of elements
    """
    total = 0
    for i in li:
        for ii in i:
            total += ii
    print(total)    # ---> display value... guiding code
    return total


t = [[1, 2], [3], [4, 5, 6]]
nested_sum(t)
