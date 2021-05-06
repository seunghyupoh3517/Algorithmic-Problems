class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """

        """
        num = [1 2 3 4]
        k   =    3 2 7 
            -----------
               1 5 6 1        
        """
        for i in range(len(num)-1,-1,-1):
            # update the num with remainder and include carry in k
            k, num[i] = divmod(k + num[i], 10)

        # if there is k then the addition has gone over the num digits, we need to 
        # appendleft the rest in k
        return [int(i) for i in str(k)] + num if k else num


if __name__ == '__main__':
    num = [9,2,3,4]
    k = 800
    print(Solution().addToArrayForm(num, k))