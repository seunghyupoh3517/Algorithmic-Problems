class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # Sliding Window, HashMap O(N)/ O(K) Hashmap
        """ 
            - store the index of unique charater in dictionary
            - two left, right pointers serving as window boundaries
            - while the window contains no more than k distinct characters
                - when len(dictionary) == k+1, move left pointer
                - while updating the maximum length            
        s = e c e b a / k = 2
            1) e:0 max = 1
            2) c:1 max = 2
            3) e:2 max = 3
            4) b:3 - k==2+1 then  
            as right append windows, save index into dictionary for each last characer
            when len(dicionary) == k+1 
                remove the leftmost which is least index in dictionary
                need to keep track of length of the string
        """
        n = len(s)
        if n * k == 0:
            return 0

        dictionary, l, r, res = {}, 0, 0, 1
        while r < n:
            # store index of character in dictonary
            dictionary[s[r]] = r
            r += 1
            # if the length of dictionary, # of unique characters, is k+1
            # then need to erase the left most character and set left pointer
            if len(dictionary) == k+1:
                delete = min(dictionary.values())
                del dictionary[s[delete]]
                # move left pointer of the sliding window
                l = delete + 1

            res = max(res, r - l)    
            
        return res

if __name__ == '__main__':
    s = "eceba"
    k = 2
    print(Solution().lengthOfLongestSubstringKDistinct(s,k))
    