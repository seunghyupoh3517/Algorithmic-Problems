class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        # Sliding Window - Find the smallesst subarray sum of length
        # O(n + k) time, O(n) takes for sum / O(1)
        """
        - Problem is comparing immediate value to add, doesn't give the accurate result
        i.e. 1 100 10 10 10, k = 2
            immediate comparison of front, back will have 20 from right 
            but max can be 101 from left two
        
        Maintain a sliding windows of size k, update max point on each iteration of adjustment
        comparing the sum of subarrays
                  k-1        n-1
        -------------  ---------
        --------------- --------
        ----------------- ------
        ------------------- ----
        ---------------------- -
        """
        n = len(cardPoints)
        if n == 1:
            return cardPoints[0]
        if k == 1:
            return cardPoints[0] if cardPoints[0] >= cardPoints[-1] else cardPoints[-1]
        
        # initialize left,right pointer
        left, right = k-1, n-1
        # initialze max
        curr_pick = sum(cardPoints[:k])
        max_pick = curr_pick

        for _ in range(k):
            curr_pick += (cardPoints[right] - cardPoints[left])
            max_pick = max(curr_pick, max_pick)
            left, right = left - 1, right - 1

        return max_pick

if __name__ == '__main__':
    cardPoints = [2,2,2]
    k = 2
    
    print(Solution().maxScore(cardPoints, k))



