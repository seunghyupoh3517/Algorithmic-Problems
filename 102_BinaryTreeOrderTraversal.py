# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        
        # BFS O(N) / O(N)
        # - Left Root Right level by level 
        result, queue = [], deque()
        if not root:
            return  []
        else:
            queue.append(root)

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
        

        # DFS O(N) / O(N + h) 
        # - track the level in the tree, simple pre-order travversal
        # - add sublists to result as we move down the levels
        def helper(root, level, result):
            if not root:
                return
            if len(result) <= level:
                result.append([])
                
            result[level].append(root.val)
            helper(root.left, level + 1, result)
            helper(root.right, level + 1, result)

        result = []
        helper(root, 0, result)
        return result

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    print(Solution().levelOrder(root))