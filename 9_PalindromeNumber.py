class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Could be one line of return statement
        """
        x = str(x)
        if x == x[::-1]:
            return True
        return False
        """

        return (str(x) == str(x)[::-1])
        

if __name__ == '__main__':
    x = -101
    print(Solution().isPalindrome(x))