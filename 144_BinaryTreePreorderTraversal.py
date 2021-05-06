# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Preorder traversal <Root Left Right>
        # Recursive way
        """
        def helper(root, result):
            if root:
                result.append(root.val)
                helper(root.left, result)
                helper(root.right, result)

        result = []
        helper(root, result)

        return result
        """     
        
        # Iteratvie way O(n), O(n)
        result, stack = [], []
        while True:
            while root:
                # append the root value first to the result
                result.append(root.val)
                # Hold on to the right value
                stack.append(root.right)
                # Traverse to the left leaf
                root = root.left

            if not stack:
                return result
            # Finsh the left branches and the root, back to right leaves
            root = stack.pop()


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print(Solution().preorderTraversal(root))