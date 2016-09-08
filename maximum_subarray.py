"""
Find the contiguous subarray within an array (containing at least one number) which has
the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

"""
Time Complexity: O(N)
Space Complexity: O(1)
Type: Dynamic Programming

Explanation:
Look at how the largest sum of an array can be determined by the largest sum of
the array excluding the last element. So, let's say we're looking at array A =
[-2, 1, -3, 4, -1, 2]. To find largest sum, we can first look at the
largest sum of array B = [-2, 1, -3, 4, -1]. The only way A's largest sum will be
different than B's is either if:
* the new value added is by itself greater than the largest sum of array B AND/OR
* the new value creates a contiguous subarray with a larger sum than the largest
  sum of array B.

In this case, the largest sum of B is 4. The new value, 2, is NOT greater than
4. However, 2 forms a contiguous subarray [4, -1, 2] which has a sum of 5
which is greater than the largest sum of B. So, keep track of if the new value
is greater than the largest sum of the smaller array (max_sum) AND/OR the new value
forms a subarray ending at this point with a sum greater than the largest sum
of the smaller array (max_sum_ending_here).

"""
def maxSubArray(self, nums):
    if len(nums) == 1:
        return nums[0]
    max_sum = num[0]
    max_sum_ending_here = num[0]
    for i in range(1,len(nums)):
        num = nums[i]
        max_sum = max(max_sum, num)
        max_sum_ending_here = max(max_sum_ending_here + num, num)
        max_sum = max(max_sum, max_sum_ending_here)
    return max_sum
