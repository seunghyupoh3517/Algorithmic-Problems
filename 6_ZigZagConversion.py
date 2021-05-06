class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # O(n) / O(n) Sorting by row and join all of them at the end
        if numRows == 1 or numRows >= len(s):
            return s

        res = [[] for i in range(numRows)]
        row = 0
        direction = -1

        for i in s:
            res[row].append(i)
            if row == 0 or row == numRows - 1:
                direction *= -1
            row += direction
        # res[0] = P A H N res[1] = A P L S I I G res[2] = Y I R

        for i in range(len(res)):
            res[i] = ''.join(res[i])
        # res[0] = PAHN res[1] = APLSIIG res[2] = YIR

        return ''.join(res)
                


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s, numRows))