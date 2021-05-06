class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        # Intuition
        """
        - one to one matching using dictionary 
        - range 0 <= num <= 2**31 - 1 == 2147483647 2biliion ..

        1: one two three ..
        10: ten twenty .. + one more pattern of 11, 12, 13 ...
        100: 1 + hundred
        1000: 1 + thousand
        10000: ten + thousand
        100000: hundred + thosand
        1000000: 1 + milion
        10000000: ten + milion
        100000000: hundred + milion
        1000000000: 1 + bilion

        Store all the integer to english representation in the dictionary
            - 123 = 1 * 100 + 2 * 10 + 3 divide and conquer?
                - Divide the number into several groups of units
                - one * hundred + two * 10 = twenty + three
        """
        # O(n) time / O(1)
        # Divide and Conquer - How to efficiently break down the problem
        """
        initial integer can be divide into three digits
        i.e.  1234567890 = 1. 234. 567. 890
              1 Bilion 234 Milion 567 Thousand 890
        Then we can reduce the initial problem to how to convert 3 digit integer to English word
        And then divide further into subproblems
        i.e.  234 -> 2 Hundred 34 then 
        """
        def one(num):
            dict_one = {
                1:'One',
                2:'Two',
                3:'Three',
                4:'Four',
                5:'Five',
                6:'Six',
                7:'Seven',
                8:'Eight',
                9:'Nine'
            }
            return dict_one.get(num)

        def less_20(num):
            dict_irregular = {
                11:'Eleven',
                12:'Twelve',
                13:'Thirteen',
                14:'Fourteen',
                15:'Fifteen',
                16:'Sixteen',
                17:'Seventeen',
                18:'Eighteen',
                19:'Nineteen'
            }
            return dict_irregular.get(num)


        def ten(num):
            dict_ten = {
                1:'Ten',
                2:'Twenty',
                3:'Thirty',
                4:'Forty',
                5:'Fifty',
                6:'Sixty',
                7:'Seventy',
                8:'Eighty',
                9:'Ninety'
            }
            return dict_ten.get(num)
        
        # i.e. one hundred + '23'
        def two(num):
            if not num:
                return  ''
            elif num < 10:
                return  one(num)
            elif num < 20:
                return less_20(num)
            else:
                tenner  = num // 10
                rest = num - tenner * 10
                return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)

        # i.e. '123' Million
        def three(num):
            hundred = num  // 100
            rest = num - hundred * 100
            if hundred and rest:
                return one(hundred) + ' Hundred ' + two(rest)
            elif not hundred and rest:
                return two(rest)
            elif not hundred and not rest:
                return one(hundred) + ' Hundred'

        # 1.234.567.890
        # 1
        billion = num // 1000000000
        # 234
        million = (num - billion  * 1000000000) // 1000000
        # 567
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        # 890
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        if not num:
           return 'Zero'
        result = ''
        if billion:
            result = three(billion) + ' Billion'
        if million:
            # if result means there is a billion need space, else, no bilion start on its own
            result += ' ' if result else ''
            result += three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)
        return result
        
if __name__ == '__main__':
    num = 123
    print(Solution().numberToWords(num))
