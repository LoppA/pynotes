# DONE
# Define a function that takes a list of lists and returns a new list of
# lists with a student's name and their average grade in each sublist.

def average_grade(lst):    
    """ Return students' names and their average grades.
    
    >>> average_grade([['Bob', 56, 80, 72, 90], ['Alice', 60, 88, 44, 70]])
    >>> [['Bob', 74.5], ['Alice', 65.5]]
    """

    ret = []

    for std in lst :
        if len(std) == 0 :
            continue

        name = std[0]
        avg = 0

        for i in range (1, len(std)) :
            avg += std[i]

        n_grade = len(std) - 1
        if n_grade > 0 :
            avg /= n_grade

        ret.append([name, avg])

    return ret
