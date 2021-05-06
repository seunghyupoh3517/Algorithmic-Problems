class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        """ O(N*K) K == length of shortest string / O(1)
        Find longest common prefix string amongst an array of strings
        if there is no common prefix return empty string " "
        - iterting the outer loop with shortest string in strs can cut down some complexity
        - 
        """
        if not strs:
            return ""

        shortest = min(strs, key = len)
        for i, char in enumerate(shortest):
            for others in strs:
                if others[i] != char:
                    return shortest[:i]
        return shortest

        
        
        



if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))