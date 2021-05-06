# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        # Use DFS to find the longest path -- all the way to the lowest level nodes O(N) / O(N) - if balanced tree O(logN)
        """
            - Longest path is between two leaf nodes which are longest left and right branches
            - Find the node of which sum of its longest left and right branch is maximized
            - Then we can use DFS to go all the way to the bottom then start count the edge upwards
                - Recursively visit children nodes and retrieve the longest path from the leaf first
                - then ad 1 to longer one before returning it as the longest path
        """
        
        self.diameter = 0
        def dfs(node):
            # end of the tree
            if not node:
                return 0 
            # traverse through the left, right branches
            left_branch = dfs(node.left)
            right_branch = dfs(node.right)

            # keep track of the maximum path, update if left + right is larger
            self.diameter = max(self.diameter, left_branch + right_branch)
            # edge connecting it with its parent (+ 1)
            return 1 + max(left_branch, right_branch)

        dfs(root)
        return self.diameter

        

        