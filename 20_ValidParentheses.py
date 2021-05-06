class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack Dictionary
        """ O(n) / O(n)
        Valid input string
            - (:) [:] {:} pair combination using dictionary
            - key: closed / value: open
            - when we see the closed, we should be able to match the open in order to validate
            - it would be better to check from the back -> stack

        i.e. ({[]}) - the sub expression of a valid expression should also be a valid expression 
        |]| what was on the top of the stack should be the match of incoming char
        |[|
        |{|
        |(| 
         __

        Corner case: what if there is single closed - temp.pop() runtime error
        """
        valid = {}
        valid[')'] = '('
        valid['}'] = '{'
        valid[']'] = '['

        stack = []
        for char in s:
            if char in valid: # if closed
                top = stack.pop() if stack else '!' # if there is stack, else assign dummy value - without value, stack.pop() runtime error
                if valid[char] != top:
                    return False

            else: # if open
                stack.append(char)

        return not stack # if not left in stack - true, else - false
            


if __name__ == '__main__':
    s = ""
    print(Solution().isValid(s))