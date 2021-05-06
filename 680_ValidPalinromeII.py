class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # O(n^2): (creating a string of length N) N times  / O(n) - time limit exceeded, Brute force solution
        """
        Given a non empty string s, i can delete at most one character, is it palindrome?
            - first check whether s is palindrome or len(s) == 1 (Base condition)
            - delete every character one by one and check whether its palindrome

        if len(s) == 1 or s == s[::-1]:
            return True
        
        temp = ""
        for i in range(len(s)):
            temp = s[:i] + s[i+1:]
            if temp == temp[::-1]:
                return True
        return False
        """

        # O(n), O(1)
        """
        Instead of checking the entire copy of string, check on each character - beginning and end using 2 pointers
        """
        if len(s) == 1:
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # a b b c a 
                s_l, s_r = s[:left] + s[left+1:], s[:right] + s[right+1:]
                return (s_l == s_l[::-1]) or (s_r == s_r[::-1])
            left += 1
            right -= 1

        return True

if __name__ == '__main__':
    input = "abc"
    print(Solution().validPalindrome(input))