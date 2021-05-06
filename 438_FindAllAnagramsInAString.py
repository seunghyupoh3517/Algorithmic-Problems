class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # By Intuition - Did not pass but similar logic
        """
        Sliding window with dictionary
        cbaebabacd
        abc
         abc
          abc ... comparing the p to s like a sliding window

        1) Iterate through p and store that in dictionary - key: p[i] value: occurence
        2) Iterate through s, check whether s[i] is in dictionary 
            - to do that, we can create another dictionary for s
            - when reaching the length of p while iterating the s, clear the s dict

        3) two index pointer of left and right
            - left, right starts from 0 
            - iterate throught the s, increment right
            - then when we meet the condition
            - update the result list with i, increment i and set right to i and repeat the steps
        """

        # Sliding window with array (instead of hashmap) - O(n+m) / O(1) constant space complexity
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []

        # 26 alphabet counter to check ==
        p_count, s_count = [0] * 26, [0] * 26

        # ord: unicode point representation of the string of length 1
        for char in p:
            p_count[ord(char) - ord('a')] += 1

        result = []
        for i in range(s_len):
            s_count[ord(s[i]) - ord('a')] += 1

            # remove one letter from the left sie of the window
            # SMART s[i - p_len]!!!!!!!!!!!!!!!!!!
            if i >= p_len:
                s_count[ord(s[i - p_len]) - ord('a')] -= 1

            # compare window, then append result with the starting index
            if p_count  == s_count:
               result.append(i - p_len + 1) 
        return result

        """
        result = []
        p_len = len(p)
        p_dict, s_dict = {}, {}

        for char in p:
            if p in p_dict:
                p_dict[char] += 1
            else:
                p_dict[char] = 1

        left, right = 0, 0
        while right < len(s):
            if s[right] in s_dict:
                s_dict[s[right]] += 1
            else:
                s_dict[s[right]] = 1

            if s_dict == p_dict:
                result.append(left)

            if right - left + 1 > p_len:            
                right = left
                left += 1
                s_dict.clear()
            right += 1

        return result
        """


if __name__ == '__main__':
   s = "ababababab"
   p = "aab"

   print(Solution().findAnagrams(s, p))