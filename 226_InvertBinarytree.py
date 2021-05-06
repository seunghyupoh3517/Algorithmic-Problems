# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Both O(n) time complexity - swap the left subtree and right subtree 
        # Recursive way
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root.val

        # Iterative way
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stacck += node.left, node.right
        return root
        

if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right= TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print(Solution().invertTree(root))
