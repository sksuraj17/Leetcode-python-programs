# Difficulty - HARD ---> Given an unsorted integer array nums, return the smallest missing positive integer. You must implement an algorithm that runs in O(n) time and uses constant extra space.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = 1
        nums.sort()
        for i in nums:
            if i == ans:
                ans += 1
        return ans
