class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        """ O(n) / O(1)
        I, V, X, L, C, D, M each representing values
        Add consecutive symbols
        written largest to smallest left to right
        Subtraction is used
            - I before V, X == 4, 9
            - X before L, C == 40, 90
            - C before  D, M == 400, 900
        """
        dict_roman = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        n, res = len(s), 0
        special = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        # V - I = - (I - V)
        for i in range(n):
            s_check = s[i:i+2] if i != n-1 else None
            if s_check in special:
                res -= dict_roman[s[i]]
            else:
                res += dict_roman[s[i]]
        return res

if __name__ == '__main__':
    s = "MCMXCIV"
    print(Solution().romanToInt(s))


        