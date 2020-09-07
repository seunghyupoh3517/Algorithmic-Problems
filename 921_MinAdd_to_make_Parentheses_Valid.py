"""https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.
Formally, a parentheses string is valid if and only if:
It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

Input: "())"
Output: 1

Input: "((("
Output: 3

Input: "()"
Output: 0

Input: "()))(("
Output: 4

S.length <= 1000
S only consists of '(' and ')' characters.
"""
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """

        if len(S) == 0:
            return 0
        
        # if there is open, append
        # if is is close, check if there has been already open so that we can match and pop
        # if there isn't which implies we need the open; thus, append
        # as we only pop one open a time whenever there is close - can count open mismatch as well
        stack = []
        for char in S:
            if char == '(':
                stack.append(char)
            else:
                if stack and stack[-1] == '(': 
                    stack.pop()
                else:
                    stack.append(char)

        return len(stack)

if __name__ == '__main__':
    str1 = "())" #1
    print(Solution().minAddToMakeValid(str1))
    str2 = "(((" #3
    print(Solution().minAddToMakeValid(str2))
    str3 = "()" #0
    print(Solution().minAddToMakeValid(str3))
    str4 = "()))((" #4
    print(Solution().minAddToMakeValid(str4))
