class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
    
        # Sliding Window O(N) / O(N)
        """
        s = ABAB k = 2 - replace two A's with two B's or vice vera
        s = AABABBA k = 1 - replace one B or A 

        1) find the longest repeating character with k replaement by taking most repeated
        chars of that subsequence and adding k
        2) max_count of answer's subsequencce - most repeated chars of that subsequence and adding k
        3) account for the subsequence by remoing the char at the start of the subsequencce 
        """
        # res: maximum length of output string
        # curr_max: max count 
        res, curr_max = 0, 0
        count = {}
        for i in range(len(s)):
            # count number of char
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
            # keep track of most repeated character count within the window
            curr_max = max(curr_max, count[s[i]]) 
            # this means we can add another char that either same or a change
            # res used as left pointer 
            if res < curr_max + k: 
                res += 1 
            else:
                # removing chars at the start of the subsequence
                count[s[i-res]] -= 1
        return res

if __name__ == '__main__':
    s = "ABAB"
    k = 2
    print(Solution().characterReplacement(s,k))