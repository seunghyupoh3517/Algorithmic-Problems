class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
       
        # Brute force O(n^2) * O(n) slicing -> Time limit exceeded
        """
        def check(s1):
            if s1 == s1[::-1]:
                return True
            return False

        res = 0
        out = ""
        n = len(s)
        for i in range(n):
            for j in range(n):
                if check(s[i:j+1]) and res < len(s[i:j+1]):
                    res = len(s[i:j+1])
                    out = s[i:j+1]
        return out
        """

        # Expand around Center O(n^2) / contant space
        # check left and right of each charater in s - check both odd, even (corner case) length

        if len(s) <= 1:
            return s

        res = ""
        res_len = 0 

        for i in range(len(s)):
            # odd length
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > res_len: # longer palinrome substring found, update
                    res = s[left:right+1] # left + (right - left + 1) = right + 1
                    res_len = right - left + 1
                left -= 1
                right += 1 

            # even length
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > res_len: 
                    res = s[left:right+1]
                    res_len = right - left + 1
                left -= 1
                right += 1 

        return res



if __name__ == '__main__':
    s = "babad"
    print(Solution().longestPalindrome(s))