#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#If target is not found in the array, return [-1, -1].
#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans1 = [-1,-1]
        res = []
        ans = []

        if target not in nums:
            return ans1
        for num in nums:
            if num == target:
                res.append(nums.index(target))
                nums[nums.index(target)] = -98965874

        ans.append(res[0])
        ans.append(res[-1])
        return ans
