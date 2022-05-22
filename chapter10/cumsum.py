def cumsum(li):
    """Cumulative sum of elements
    in a list

    li: list of ints

    returns: new list
    """
    total = 0
    new_li = []
    for i in li:
        total += i
        new_li.append(total)
    print(new_li)
    return new_li

t = [1, 2, 3]
cumsum(t)   # [1,3,6]
