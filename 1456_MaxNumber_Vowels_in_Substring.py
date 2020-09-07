"""https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
Given a string s and an integer k.
Return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are (a, e, i, o, u).

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Input: s = "rhythms", k = 4
Output: 0
Explanation: We can see that s doesn't have any vowel letters.

Input: s = "tryhard", k = 4
Output: 1

1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= s.length
"""
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxCount = currCount = 0
        # state the string of vowels to compare
        vowels = "aeiou"

        # sliding window technique to check all the substrings
        for index, value in enumerate(s):
            # from first k size of s part after that every index it operates to check the substring
            # after checking the first window size, every increment in index will check 
            if index >= k:
                # if next substring, the first element of previous window had vowel decrease 1 from the counter
                if s[index - k] in vowels:
                    currCount -= 1
            # if it's vowel, add 1 to counter / check all the char
            if s[index] in vowels:
                currCount += 1
            # update the count to find maximize
            maxCount = max(currCount, maxCount)

        return maxCount
        
if __name__ == '__main__':
    s = "abciiidef"
    k = 3
    print(Solution().maxVowels(s,k))

    s = "aeiou"
    k = 2
    print(Solution().maxVowels(s,k))

    s = "leetcode"
    k = 3
    print(Solution().maxVowels(s,k))

    s = "rhythms"
    k = 4
    print(Solution().maxVowels(s,k))

    s = "tryhard"
    k = 4
    print(Solution().maxVowels(s,k))
