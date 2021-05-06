class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        

        """
        m X n board of characters and list of string words
        adjacent cells - horzontal, vetical, cell used only once
        -> check if we can make words in word list within the m X n board

        1) Build trie dictionary out of words in wordList - will be used for the matching process later
        2) Starting from each cell, start backtracking exploration
            - if there exists any word in the wordlist that starts with the letter in the cell
        3) At each call, we check if the sequence of letters that we traverse matchtes any
        word in the dictionary. 
        """
        

