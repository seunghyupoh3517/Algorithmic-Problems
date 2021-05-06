# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """
class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        
        """
        list of words ["abc","aaa", ...], one word chosen from the list, secret
        10 guesses to have # of matching word = return integer for corresponding value/location
        
        < Simple guessing game, remove the candidates which does not match the clue >
            1) randomly choose the word from the wordlist and guess the word
            2) (if matching != 6) remove the word and remove the word whcih don't have exactly # characters in common with guess
            3) keep 1),2)
            - minimizing the wordlist and narrow down the canidates 
        """
        # using set to pop() the word randomly
        wordIndices = set(range(len(wordlist)))

        def findScore(word1, word2):
            score = 0
            for i in range(len(word1)):
                if word1[i] == word2[i]:
                    score += 1
            return score

        while wordIndices:
            # set pop() randomly retrieve the value
            wordIndex = wordIndices.pop()
            wordGuess = wordlist[wordIndex]
            guessScore = master.guess(wordGuess)

            wordIndices = {i for i in wordIndices if findScore(wordGuess, wordlist[i]) == guessScore}
            """
            if len(wordIndices) == 1:
                index = wordIndices.pop()
                return wordlist[index]
            """
        
