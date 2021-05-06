class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # By intuition
        """ 
        a a b b c c c -> a2b3c3 -> 6
        a b b c -> ab2c -> 4
        iterate through the chars
        |b|
        |b|
        |a|
        |a| can detect whether the consecutive charcter has change or not: if stack[-1] == char in chars
        ___ if so - keep add to stack, if not hold on to adding and pop until no more char left and with counter value 
        
        Also, need to update the given chars leave the first item, and rest popleft to delete
        """

        # Two Pointers
        """
        Outerloop: iterate the chars
        Innerloop: count the frequency of same character
        """
        left, write = 0, 0
        while left < len(chars):
            # Keep the first character in chars
            char, frequency = chars[left], 1
            # while the following char is same char, count the commonn character
            while left + 1 < len(chars) and char == chars[left + 1]:
                left += 1
                frequency += 1
            
            # only if frequency is greater than 1, we put frequency
            if frequency > 1:
                # 12 = '1', '2'
                for ch in str(frequency):
                    chars[write+1] = ch
                    write += 1

                i = 0
                while frequency - write - i > write:
                    del chars[frequency - write - i]
                    i += 1
                    left -= 1
                
            left += 1
            write +=1
            
        return chars


if __name__ == '__main__':
    chars = ["a", "a", "a", "a", "b", "b", "a", "a"]
    print(Solution().compress(chars))