class Solution(object):
    # Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return 0
        
        if x > 0:
            result = str(x)[::-1]        
        else:
            result = "-" + str(abs(x))[::-1]   
        
        
        result = int(result)
        if result > (2 ** 31 - 1) or result < -(2 ** 31) or  result == 0:
            return 0 
        else: 
            return result



if __name__ == '__main__':
    x = -123
    print(Solution().reverse(x))