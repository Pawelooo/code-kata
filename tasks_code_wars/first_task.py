"""
An isogram is a word that has no repeating letters,
consecutive or non-consecutive. Implement a function that determines
whether a string that contains only letters is an isogram. Assume the empty
string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)


isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false

"""

from collections import Counter


def is_isogram(string):
    cnt = Counter()
    if string is None:
        return True, "an empty string is a valid isogram"
    for val in string:
        if val.lower() in cnt:
            return False
        if val in cnt:
            return False, "same chars may not be adjacent"
        if val.capitalize() in cnt:
            return False
        cnt[val.lower()] += 1
    return True
