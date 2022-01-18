def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    res = True
    for l in lst:
        res = res and isinstance(l,list)

    return res
