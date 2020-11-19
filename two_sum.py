"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = nums
        target = target
        seen = {}
        y = []
        for counter, num in enumerate(nums):
            remain = target - num

            if remain in seen:
                return [seen[remain], counter]
            seen[num] = counter
        return y

cl = Solution()
print('/n next')
print(cl.twoSum([2, 7, 11, 15], 18))
print(cl.twoSum([3, 2, 4], 6))
print(cl.twoSum([3, 3], 6))
print(cl.twoSum([4, 4, 4], 8))
