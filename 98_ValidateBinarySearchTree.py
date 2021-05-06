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
        # Recursive way O(n), O(n) of checking all nodes / keeping up the entire tree
        def helper(root, low = float('-inf'), high = float('inf')):
            if not root:
                return True

            if root.val <= low or root.val >= high:
                return False
            
            # Check left subtree and right subtree - update the low and high value
            # left subtree - now high is root value, right subtree - now low is root value
            else:
                return helper(root.left, low, root.val) and helper(root.right, root.val, high)
        return helper(root)

        
       

if __name__ == '__main__':
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.left = TreeNode(1)
    print(Solution().isValidBST(root))
        


