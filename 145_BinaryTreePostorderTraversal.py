# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Postorder <Left Right Root>
        # Recursive way
        """
        def helper(root, result):
            if root:
               helper(root.left, result)
               helper(root.right, result)
               result.append(root.val)
        result = []
        helper(root, result)

        return result
        """

        # Iterative way O(n) O(n)
        result, stack = [], []
        
        while True:
            while root:
                # Fill up the stack with Right -> Node -> Left order
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root  = root.left

            if not stack:
                return result

            node =  stack.pop()
            # If the right tree hasn't been processed yet before the root, 
            # then push the root node back into stack and process right node first 
            if stack and stack[-1] is node.right:
                root = stack.pop()
                stack.append(node)
            else:
                result.append(node.val)


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    # 3 2 1
    print(Solution().postorderTraversal(root))