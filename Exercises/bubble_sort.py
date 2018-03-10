# DONE
# Use bubble sort to solve this problem.
# Wiki on the algorithm at https://en.wikipedia.org/wiki/Bubble_sort


def bubble_sort(numbers):
    """ Use bubble sort to sort a list of numbers in ascending order.
        Return the input list after mutating it with sorted numbers.
    
    >>> bubble_sort([2, 19, 4, 1, -40])
    [-40, 1, 2, 4, 19]
    >>> 
    """

    n = len(numbers)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if (numbers[j] > numbers[j+1]):
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers
