"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result = line[:]
    result.sort(key=lambda v: v == 0)
     
    
    for key, number in enumerate(result):
        try:
            if number == result[key + 1] and number is not 0:
                result[key] = 2 * number
                result[key + 1] = 0

        except IndexError:
            pass
    
    result.sort(key=lambda v: v == 0)

    return result