'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        d = {'{':'}','(':')','[':']'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif (len(stack) == 0 or d[stack.pop()] not in i):
                return False
        return (not stack)

                
