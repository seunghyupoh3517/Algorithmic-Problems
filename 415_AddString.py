class Solution(object):
    # Without any built in library or converting the inputs to integer directly
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # O(max(N1, N2)) / O(max(N1,N2))
        # Addition on each character from the end - consider carry '1' or '0'
        len_1 = len(num1) - 1
        len_2 = len(num2) - 1
        res, carry = [], 0
        
        # from the end
        while len_1 >= 0 or len_2 >= 0:
            val1 = ord(num1[len_1]) - ord('0') if len_1 >= 0 else 0
            val2 = ord(num2[len_2]) - ord('0') if len_2 >= 0 else 0
            carry, remainder = divmod(val1+val2+carry, 10)
            res.append(remainder)
            
            len_1 -= 1
            len_2 -= 1
        
        # if there's additional digit created, append another digit if so 
        if carry:
            res.append(carry)

        # Reverse, make integer in list to string   
        return ''.join(str(x) for x in res[::-1])

if __name__ == '__main__':
    num1 = "456"
    num2 = "77"
    print(Solution().addStrings(num1, num2))