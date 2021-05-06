from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        # Intuition, Sliding Window O(|S| + |T|) / O(|S| + |T|)
        """
        s = ADOBECODE BANC t = ABC
        output = BANC minimum window which will contain all the characters in t
            - will t have duplicate characters?

        1) Store chars in t with counter dictionary
        2) By using left, right pointers and append the window size in s until I get all characters in t from s
            - keep track of the size of the window so to get the minimum window size
            - append the window with right, move left pointer when we get all the characters and update minimum length
        3) return the minimum length of window -> try to contract the window size, update the variables
        * if there is duplicates in t, I cannot simply check the length of dict_t since that only counts numbers of unique characters in t
        thus need to check if dict_t[char] == dict_window[char] then we can make sure
        """
        # Base condition
        if not t or not s:
            return ""

        dict_t, dict_window = Counter(t), {} # required only checks number of unique characters so need to check if the val is same
        required, formed = len(dict_t), 0
        left, right, min_len, min_s = 0, 0, float('inf'), ""
        min_left, min_right = 0, 0

        while right < len(s):
            curr_char = s[right]
            dict_window[curr_char] = dict_window.get(curr_char, 0) + 1

            if curr_char in dict_t and  dict_window[curr_char] == dict_t[curr_char]:
                formed += 1
            
            # if the current window has all the characters in t, let's try to contract the
            # window in order to find the minimum length
            while left <= right and required == formed:
                # update the minimum window 
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left, min_right = left, right + 1
                    # min_s = s[left:right+1] - slicing will take O(k)
                
                # character at left pointer no longer part of window 
                remove_char = s[left]
                dict_window[remove_char] -= 1
                # if removing char happens to make no longer containing all characters in t
                if remove_char in dict_t and dict_window[remove_char] < dict_t[remove_char]:
                    formed -= 1
                # try to contract the window size
                left+= 1

            # appending the window
            right += 1
        return s[min_left:min_right]    

        # Small improvement
        """
        Having filtered s which has all the chcaracters from string s along with their indicces in s 
        that the characters is in t
        """

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))