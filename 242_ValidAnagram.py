from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # O(n) 
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s,t))