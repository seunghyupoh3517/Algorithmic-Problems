class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Stack O(n) / O(n)
        """
        Brute Force way could be done passing all the substring to validation - O(n^2 * n)
        Instead of finding every possible string and validate, use Stack to scan an check validity at the same time

        Stack with -1 to start - sort of utilizing a pointer index
        every (, push its index
        every ), pop the topmost element and subtract the current index = which gives the length of the current valid string

        if stack become empty, we push the current index onto the stack 
        """


        """
        Validation + longest substring 
            - could think of stack validation
            - corner case when empty stack 
            - how to calculate the length (Sort of sliding window approach, from the index where until last valid index which is left, current index is right
                then "right - left" needs another +1 in order to calculate the length correctly - thus, add the first element of -1 to the stack)
        """
        res = 0 
        stack = [-1]

        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            else:
                # to remove the matching open parentheses 
                stack.pop()
                # which indicates invalid encounter thus update last valid parentheses index which will be current index
                if not stack:
                    stack.append(index)
                # if the valid string then update the longest length
                else:
                    res = max(res, index - stack[-1])
                
        return res
        
       


        
if __name__ == '__main__':
    s = ")()())"
    print(Solution().longestValidParentheses(s))