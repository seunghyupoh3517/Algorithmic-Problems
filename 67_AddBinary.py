class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # Binary Operation O(max(N,M)) / O(max(N,M))
        """
        1100
        0101
        ----
        10001
        
        n = max(len(a), len(b))
        # fill up 0's for binary operation 
        a, b = a.zfill(n), b.zfill(n)
        # iteration from backward
        ans, carry = [], 0
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            
            if carry % 2 == 0:
                ans.append('0')
            else:
                ans.append('1')

            carry = carry // 2
        
        if carry == 1:
            ans.append('1')
        ans.reverse()

        return ''.join(ans)
        """

        # Bit manipulation O(N+M) / O(max(M,N))
        # & AND, | OR, ^ XOR, ~ NOT, a << n, a >> n
        # bin(): converts and return the binary equivalent stirng of integer i.e. 0bxxx
        """
         1101  a ^ b = 1110 answer without carry
         0011  (a & b) << 1 = 0010 carry
        -----
        10000
        """
        a, b = int(a, 2), int(b, 2)
        while b:
            answer = a ^ b
            carry = (a & b) << 1
            a, b  = answer, carry
        return bin(a)[2:]


if __name__ == '__main__':
    a = "11"  
    b = "1"
    print(Solution().addBinary(a,b))