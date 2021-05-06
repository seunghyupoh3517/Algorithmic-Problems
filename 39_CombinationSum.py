class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # Backtracking - checking all possible candidates 
        """
        - Path: [] / Add the each one element to the path and send rest to next helper functon
                   / if condition to check for each path iteration whether the sum of path exceed the target
                    or it has reacehd the target
                   / if the sum == target, append path to the result 
                   / if it exceeded, stop the further branch
        - visited: set() / when appendin the path to the result, check whether the path already has been seen
                         / if not, add to the result 

        candidates = [2,3,6,7] target = 7
        output = [[2,2,3], [7]]
        2 - 2 - 2 - 2 X  3 - 2 O
                  - 3 X    - 3 X
                  ..       ..
              - 3 O
          - 3 - 2 O
              - 3 X
              ...
          - 6 X
          - 7 X
        """

        """ - faild avoiding the duplicate combinations
        if not candidates or not target:
            return []
        
        res, visited = [], set([])
        def backtracking(index, path):
            if sum(path) > target:
                return
            
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                # same element can be used unlimited times, send same current i
                backtracking(i, path)
                path.pop()
                ## Cannot add a list to a set because lists are mutable - list not hashable
            if sum(path) == target:
                #visited.add(path[:])
                res.append(path[:])
        backtracking(0, [])
        return res
        """
        
        if not candidates or not target:
            return []

        res = []
        def backtracking(remain, index, path):
            if remain < 0:
                return
            if remain == 0:
                res.append(path[:])
                return
            
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                backtracking(remain - candidates[i], i, path)
                path.pop()

        backtracking(target, 0, [])
        return res
       
    
if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7

    print(Solution().combinationSum(candidates, target))

