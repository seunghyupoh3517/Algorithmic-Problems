class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # How to achieve O(n) / O(1)?
        """ 
            - considering only alphanumeric characters and ignore other cases
                - when iterating the string, use .isalnum() to check if its considering cases
            - use two pointers, left and right 
                - palindrome is language that words backware and forward the same 
                - by using two pointers we can check each end while iterating the string
        """
        if not s:
            return s
        
        left, right = 0, len(s) - 1
        while left < right:
            # check left end
            while not s[left].isalnum() and left < right:
                left += 1

            # check right end
            while not s[right].isalnum() and left < right:
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            else:
                left, right = left + 1, right - 1

        return True

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))