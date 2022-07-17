'''
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.
'''

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        if indices == sorted(indices):
            return s
        list1 = [''] * len(s)
        for i in range(len(s)):
            list1[indices[i]] = s[i]
        return "".join(list1)
