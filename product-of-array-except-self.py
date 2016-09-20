"""
Given an array of n integers where n > 1, nums, return an array output such that output[i]
is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
"""
def product_except_self(nums):
    if len(nums) <= 1:
        return -1
    n = len(nums)
    product_from_start = [1] * n
    product_from_end = [1] * n
    for i in xrange(1,len(nums)):
        product_from_start[i] = product_from_start[i-1] * nums[i-1]
        product_from_end[n-1-i] = product_from_end[n-i] * nums[n-i]
    ret = []
    for i in xrange(0,n):
        ret.append(product_from_start[i] * product_from_end[i])
    return ret
