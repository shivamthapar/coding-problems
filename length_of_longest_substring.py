"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer
must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
Runtime Complexity: O(N)
Space Complexity: O(N)

Two-pointer. Use two pointers: start and end. Use a hash map to keep track of which
characters have appeared in the current substring. If the char at end doesn't
exist in the current substring, add it to the current substring and increment
end. If it's a duplicate character, increment the start pointer and remove
characters from the front, until start points after the duplicate character (needs rewording).

i.e.
original string: abcabcd

a
ab
abc
 bca
  cab
   abc
   abcd  -> length = 4
"""
def lengthOfLongestSubstring(s):
    if len(s) <= 1:
        return len(s)
    n = len(s)
    char_map = {}
    start = 0
    end = 0
    max_len = 0
    while end < n:
        c = s[end]
        if c not in char_map:
            char_map[c] = 1
            max_len = max(max_len, end - start + 1)
            end += 1
        else:
            char_map.pop(s[start], None)
            start += 1
    return max_len
