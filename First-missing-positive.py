class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = 1
        nums.sort()
        for i in nums:
            if i == ans:
                ans += 1
        return ans
