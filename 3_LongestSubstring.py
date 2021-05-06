class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Brute force - checking all the substrings with no repeating characters and return the max length one
        """
        def check(start, end): # checking whether the substring has repeating chatacters 
            duplicate = [0] * 128 # list of 128 ASCII Unicode characters with default value 0 
            for i in range(start, end + 1):
                c = s[i]
                if duplicate[ord(c)] > 0:
                    return False
                duplicate[ord(c)] += 1

            return True

        n = len(s)
        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                if check(i, j):
                    result = max(result, j - i + 1)
        return result
        """

        # Sliding window - using hash set, [i, j) slide the window until the s[j] is in the hashset
        # To optimize, use mapping to make operation efficiently by knowing where to start again when repeated character occur
        result = i = j = 0
        n = len(s)
        duplicate = {}

        for j in range(n):
            if s[j] in duplicate:
                i = max(i, duplicate[s[j]])
            
            result = max(result, j - i + 1)
            duplicate[s[j]] = j+1

        return result

        
if __name__ == '__main__':
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))