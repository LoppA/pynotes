# DONE
# Create a function that returns a dictionary of the items of a list
# and their counts.

def count_items(lst):    
    """ Return counts of the list items.
    
    >>> count_items(['one', 'two', 'two', 'three', 'three', 'three'])
    >>> {'one': 1, 'three': 3, 'two': 2}
    """

    dct = {}

    for item in lst:
        if item not in dct:
            dct[item] = 0
        dct[item] += 1

    return dct
