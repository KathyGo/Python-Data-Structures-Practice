def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    lst = []
    for p in parens:
        if p == '(':
            lst.append(p)
        elif p == ')':
            if len(lst) == 0:
                return False
            lst.pop()
    
    if len(lst) == 0:
        return True
    
    return False
    