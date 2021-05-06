# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Use Inorder traversal to generate a list of elements in ascending order - could be done both in recursive and iterative way
        # Can optimize iteratvie way to O(H+K) from O(n) time complexity and O(H) space complexity
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left

            root  = stack.pop()
            #  # instead of appending to the result in the inorder traversal  - K statement
            k -= 1
            if not k:
                return root.val
              
            root = root.right

        

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)
    k = 1

    print(Solution().kthSmallest(root, 1))