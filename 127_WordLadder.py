from collections import defaultdict, deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        hit = *it / h*t / hi*
              differ by a single letter
              x / hot / x
              hot = *ot / h*t / ho*
                    dot / x / x
                    dot = *ot / d*t / do*
                          lot / x / dog
                          ... 
        """

        def preprocess(wordList):
            wordDict = defaultdict(list)
            for word in wordList:
                for i in range(len(word)):
                    key = word[:i] + '*' + word[i+1:]
                    wordDict[key].append(word)
            return wordDict

        wordDict = preprocess(wordList)
        queue = deque([(beginWord, 1)])
        visited = {beginWord:True}

        while queue:
            current_word, level = queue.popleft()
            for i in range(len(current_word)):
                intermediate_word = current_word[:i] + '*' + current_word[i+1:]

                for word in wordDict[intermediate_word]:
                    if word == endWord:
                        return level + 1

                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level+1))
                    wordDict[intermediate_word] = []

        return 0

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(Solution().ladderLength(beginWord, endWord, wordList))