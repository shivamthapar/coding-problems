"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
"""

"""
Time Complexity: O(N)
Space Complexity: O(N)
"""
def isAnagram(s,t):
    if len(t) != len(s):
        return False
    char_map = {}
    for letter in s:
        if letter not in char_map:
            char_map[letter] = 0
        else:
            char_map[letter] += 1
    for letter in t:
        if letter not in char_map:
            return False
        char_map[letter] -= 1
    for letter in char_map:
        if char_map[letter] != 0:
            return False
    return True
