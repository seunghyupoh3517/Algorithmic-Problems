"""https://leetcode.com/problems/validate-binary-search-tree/
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root, min = float('-inf'), max = float('inf')): # initializing value as infinity for minimum, maximum
            if not root:
                return True

            val = root.val # checking the root value
            if val <= min or val >= max:
                return False
            
            # pass on to left / right subtree with updated bound
            if not helper(root.left, min, val):
                return False
            if not helper(root.right, val, max):
                return False
            return True

        return helper(root)

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    
    root1 = TreeNode(5)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.right.left = TreeNode(3)
    root1.right.right = TreeNode(6)
    
    print(Solution().isValidBST(root))
    print(Solution().isValidBST(root1))