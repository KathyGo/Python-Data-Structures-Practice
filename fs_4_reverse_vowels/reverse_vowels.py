def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = [c for c in s if c.lower() in 'aeiou']
    lst = list(s)
    vowels.reverse()
    
    for j in range(0, len(lst)):r
        if lst[j].lower() in 'aeiou':
            lst[j] = vowels[0]
            vowels = vowels[1:]
            # print('vowels', vowels)
            # print('lst', lst)

    return ''.join(lst)