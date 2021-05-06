# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        # Depth First Search O(N) / O(N) 
        # Recursive
        """
        self.res = 0
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.res += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)
        
        dfs(root)
        return self.res
        """
        # Iterative
        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    res += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)

        return res

if __name__ == '__main__':
    root = [10,5,15,3,7,null,18]
    low = 7
    high = 15

    print(Solution().rangeSumBST(root,low,high))