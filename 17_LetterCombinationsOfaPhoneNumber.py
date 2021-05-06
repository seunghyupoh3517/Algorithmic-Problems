class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        # Backtracking O(N*4^N) time / O(N) space recursion call stack
        #  N: length of digits, 4 indicates maximum value length in hash map
        """
        Given a string containing digits from 2 - 9 // No need to worry about 0 and 1
        1) First put all the digits with corresponding chars into dictionary 
        2) send to the backtracking
            - for each number in digits, look up each number on the dictionary 
            - if the one done send recursively pass it on to next backtrackng

        234 (abc, def, ghi): a - d - g then b ...
                                   - h
                                   - i 
                               - e 
                                   - g
                                   - h
                                   - i
                               - f
                                   - g
                                   - h
                                   - i
        """
        if not digits:
            return []
        res = []

        phone_book = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        def backtracking(index, path):
            # Base condition to stop 
            if len(path) == len(digits):
                res.append(''.join(path))
                return # backtrack
            # append and pop
            letters = phone_book[digits[index]]
            for letter in letters:
                path.append(letter)
                backtracking(index+1, path)
                path.pop()

        # backtracking helper of starting index, updating the path added to the result
        backtracking(0, [])
        return res

if __name__  == '__main__':
    digits = "23"
    print(Solution().letterCombinations(digits))