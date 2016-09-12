"""
Given two positive integers x and y, find x^y.
"""
"""
Runtime complexity: O(log y)
Space complexity: O(1)

Reference: https://en.wikipedia.org/wiki/Exponentiation_by_squaring
Use the fact that:
x ^ y = {   x(x^2)^((y-1)/2) if y is odd
            (x^2)^(y/2)      if y is even
        }
"""
def power(x,y):
    ret = 1
    while y > 1:
        if y%2 == 0: #if even
            y /= 2
        else:        #if odd
            ret = x
            y = (y-1)/2
        x *= x
    return ret * x
