class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        """
        By intuition, i will have to keep track of how many time a char ouccur - whether it reaches k
        I still need to remove duplicates from the back -> stack
        """
        stack = []
        for char in s:
            # 
            if stack and stack[-1][0] == char and stack[-1][1] + 1 == k:
                stack.pop()
            elif stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
        
        result = ""
        # append char * occurence 
        for i in stack:
            result += i[0] * i[1] # a * 2 = aa

        return result

if __name__ == '__main__':
    input = "deeedbbcccbdaa"
    k = 3 
    print(Solution().removeDuplicates(input, k))