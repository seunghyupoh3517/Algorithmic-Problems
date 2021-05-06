# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Inorder traversal <Left Root Right>
        # Recursive way O(n) O(n)
        """
        def helper(root, result):
            if root:
                helper(root.left, result)
                result.append(root.val)
                helper(root.right, result)

        result = []
        helper(root, result)
        if not root:
            return result

        return result
        """
        # Iteratvie way O(n) O(n)
        result, stack = [], []
        while True:
            # Push root to stack - hold on to root and traverse to left leaves
            while root:
                stack.append(root)
                root = root.left
            
            # if no root value stored left, return the result
            if not stack:
                return result
            
            # Pop the stack when reach the left end and add to the result, traverse to right
            node = stack.pop()
            result.append(node.val)
            root = node.right

        return result
   
if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print(Solution().inorderTraversal(root))