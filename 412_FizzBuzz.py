class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = [""] * n # Or I can just append 
        for i in range(n):
            if (i+1) % 15 == 0:
                answer[i] = "FizzBuzz"
            elif (i+1) % 3 == 0:
                answer[i] = "Fizz"
            elif (i+1) % 5 == 0:
                answer[i] = "Buzz"
            else:
                answer[i] = str(i+1)
        return answer

if __name__ == '__main__':
    n  = 15
    print(Solution().fizzBuzz(n))