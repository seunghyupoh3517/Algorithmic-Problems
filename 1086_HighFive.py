from collections import defaultdict
class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        result, dictionary = [],  defaultdict(list)
        for item in items:
            dictionary[item[0]].append(item[1])
        
        for k,v in dictionary.items():
            v.sort(reverse=True)

        for k,v in dictionary.items():
            avg = 0
            for i in range(5):
                avg += v[i]
            result.append([k, avg/5])

        return result

if __name__ == '__main__':
    items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    print(Solution().highFive(items))