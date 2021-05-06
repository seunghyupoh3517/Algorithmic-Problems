class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        # Backtracking
        """
        Validation:
            - openning : closing ==
            - when encountering  closing: there should be unmatched openning parentheses
            - Valid can be formed from invalid
                -> so we just simply need to make them valid

        Which bracket to remove:
            - try all the option 
            - at each bracket, either part of the final or be ignored

        Minimum removal:
            - Multiple ways to make invalid to valids
            - Multiple brackets removal but it could yield same valid expression
        
        # Brute force way of Backtracking 
        1) Initialize an array that will store all of valid expression finally
        2) Start with the leftmost bracket in the given sequence and proceed right in the recursion
        3) The state of  recursion is defined by the index which we are currently in the original expression
            - left_count, right_count represent number of left, right parentheses we added to our expression
        4) If the current charater is neither closin or opening, simply add thi character to final olution
        5) If the current character is either closing or opening, then we have two options
            - discard this chracter
            - part of the final expression
        6) Validation if left_count == right_count
            - to keep track of # of removals, another variable passed in recurssion, rem_count
            - if rem_count < least # of steps to form valid expression (global minima)
        
        * Pruning needed to optimize
          for a closing parenthesis, we check if right_count < left_count

        => Tweak way to implement more efficiently
        1) Count numbers of mismatching parentheses first
            - if mismatching == 0: valid parentheses, return
            - if not we can still use to check the minimum number of removals   
        2) DFS way of backtracking with visited set() in order to avoid duplicates, also pruning 
        of further backtracking 
        """

        def mismatched(s):
            # count invalid left, right parentheses
            left, right = 0, 0
            for char in s:
                if char == '(':
                    left += 1
                elif char == ')':
                    # if right parentheses - if left == 0, then invalid right parentheses
                    right = right + 1 if left == 0 else right
                    # if right parentheses, it could be a possible matching with left parentheses
                    # then it cancel out another left parentheses but if left <= 0, invalid right parentheses
                    # which will be covered in previous if statement so leave left as it is
                    left = left - 1 if left > 0 else left
            # count total number of invalid parentheses for given string
            return left + right

        def DFS(s):
            # no invalid parentheses, then return the string
            mis = mismatched(s)
            if mis == 0:
                return [s]

            ans =  []
            # iterate through the s
            for i in range(len(s)):
                # remove whatever parenheses
                if s[i] == '('  or s[i] == ')':
                    part = s[:i] + s[i+1:]
                    # Pruning
                    # new substring not seen and (numbers of invalid parenthesess - which means # of removals)
                    # - minmum removals string 
                    if part not in visited and mismatched(part) < mis:
                        visited.add(part)
                        # Pass to further removal - ultimately, returned and appended when string is valid (mis == 0)
                        ans.extend(DFS(part))
            
            return ans

        # Avoid duplicates
        visited = set([])
        return DFS(s)

if __name__ == '__main__':
    s = "()())()"
    print(Solution().removeInvalidParentheses(s))