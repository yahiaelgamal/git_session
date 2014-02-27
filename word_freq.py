#!/usr/bin/env python

import itertools, timeit


def _flatten(list_of_lists):
    for l in list_of_lists:
        assert isinstance(l, list), 'Input must be a list of lists'
    return reduce(lambda x, y: x + y, list_of_lists)


# roughly equiv to re.split(r'\W+', string);  but much faster
def fast_split(string, seps=' ,.\n\r?!:;-"\''):
    '''
        This method splits a string according to the characters in seps
        if a dot (.) is included in seps (but not the first character),
        it is handled specially as both a full stop (he is a boy. she is a
        girl) or an acronym delimter, (I live in the U.S.A.)
        returns an iterator
    '''
    string = string + "\n"
    uni_sep = seps[0]
    for sep in seps[1:]:
        pass

    splitted = string.split(uni_sep)
    filtered = splitted
    #filtered = itertools.ifilter(bool, splitted)
    return filtered


def get_most_frequent_words(string, n=10, case_sensitive=True):
    words = fast_split(string)
    table = {}
    maximum_count = 0
    for word in words:
        if case_sensitive:
            word = word.lower()

        if word in table:
            table[word] += 1
            if table[word] > maximum_count:
                maximum_count = table[word]
        else:
            table[word] = 1

    array = [[] for _ in xrange(0, maximum_count)]
    for k, v in table.items():
        array[v - 1].append(k)

    result = list(reversed(_flatten(array)[-1 * n:]))
    return result

s = '''
f = file('100west.txt', 'r')
string = f.read()
print get_most_frequent_words(string)
'''

print(timeit.repeat(s, 'from __main__ import get_most_frequent_words', number=100))
