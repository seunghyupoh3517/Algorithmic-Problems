
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        """
        When adding another character to the result when going through S,
        Check whether the character that I am about to append is same as the character
        which were in it already
        -> Comparing with the last element -> Stack
        """
        result = []
        for char in S:
            if result and char == result[-1]:
                result.pop()
            else:
                result.append(char)

        return ''.join(result)
        

if __name__ == '__main__':
    input = "abbaca"
    print(Solution().removeDuplicates(input))