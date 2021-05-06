class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        """ Letter / Digit logs = Identifier + ...
        1) letter logs then digit logs
        2) letter logs -  lexicographically order on values, identifiers
        3) digit logs - maintain
        """
        # O(M N log N) comparison between two keys O(M) * sorted() / O(M N) to keep the keys for the log
        def new_key(log):
            # divide logs into identifier and contents, maxsplit = 1
            id, rest = log.split(" ", 1)
            
            if rest[0].isalpha():
                return (0, rest, id)
            else:
                return (1, )

        return sorted(logs, key = new_key)



if __name__  == '__main__':
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    print(Solution().reorderLogFiles(logs))