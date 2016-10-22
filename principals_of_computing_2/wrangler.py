"""
Student code for Word Wrangler game
"""

import urllib2
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    result = []

    for item in list1:
        if item not in result:
            result.append(item)

    return result

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    result = []

    for item in list1:
        if item not in result and item in list2:
            result.append(item)

    return result

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    result = []    
    lista = list1[:]
    listb = list2[:]

    while lista and listb:
        if lista[0] <= listb[0]:
            result.append(lista.pop(0))
        else:
            result.append(listb.pop(0))

    return result + lista + listb
    

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <= 1:
        return list1

    list_a, list_b = list1[:len(list1)/2], list1[len(list1)/2:]
    sorted_list_a, sorted_list_b = merge_sort(list_a), merge_sort(list_b)
    return merge(sorted_list_a , sorted_list_b)

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
        
    if len(word) < 1:
        return [word]

    first_letter, rest = word[0], word[1:]
    rest_strings = gen_all_strings(rest)

    new_strings = []
    for string in rest_strings:
        new_string_list = [string[:i] + first_letter + string[i:] for i in range(len(string) + 1)]
        new_strings.extend(new_string_list)
    
    rest_strings.extend(new_strings)
    return rest_strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()
