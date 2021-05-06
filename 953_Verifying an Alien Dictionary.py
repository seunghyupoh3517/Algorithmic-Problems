class Solution(object):
    def isAlienSorted(self, words, order):

        """
        Comparing adjacent word in words lexicographically
        """
        # Save order in dictionary to check the order using its index
        order_map = {}
        for index, char in enumerate(order):
            order_map[char] = index
        
        # Check adjacent word in words and compare lexicographically
        # words = [word1, word2 ... ]
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                # correct order: app, apple
                if j >= len(words[i+1]):
                    return False

                # if the character is not same, former word[] has to have less value, higher order
                if words[i][j] != words[i+1][j]:
                    if words[i][j] > words[i+1][j]:
                        return False
                    # if we find the letter is different and in sorted order, then no need to further check
                    # other characters
                    break

        return True
        

if __name__ == '__main__':
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(Solution().isAlienSorted(words, order))