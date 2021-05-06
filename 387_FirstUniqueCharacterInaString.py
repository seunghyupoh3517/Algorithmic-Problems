from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # O(n) / O(1) : 26 english characters (contstant space) string to dictionary of 26 english characters - O(26)
        # Using dictionary to check which character is unique character - frequency = 1
        # Comparision while iterating the s and return the first index
        count = Counter(s)
        for counter, char in enumerate(s):
            if count[char] == 1:
                return counter
        return -1
        
if __name__ == '__main__':
    s = "leetcode"
    print(Solution().firstUniqChar(s))
