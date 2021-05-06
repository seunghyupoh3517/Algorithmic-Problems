# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # Recursvie - O(n) traverse the entire input tree / O(n) - nnumber of height of the tree
        """
        A tree is symmetric if the left subtree is a mirror reflection of a right subtree 
        => When are two trees a mirror reflection of each other?
            1. their two roots have the same value
            2. the right subtree of each tree is a mirror reflection of the left subtree of the other tree

            1   root
           2 2  root.left == root.right
         3 4 4 3    root.left.left == root.right.right and root.left.right == root.right.left

         => Then when they are not symmetric beside those?
            if root.left == None and root.right == None : then True symmetric But
            if root.left == None or root.right == None : then False
            
            1 
           2 2
         3 x 3 x False
        """

        """
        def helper(l, r):
            if not l and not r: return True
            if not l or not r: return False
            return (l.val == r.val) and helper(l.left, r.right) and helper(l.right, r.left)

        return helper(root, root)
        """

        # BFS Approach, Iterative way - Iterative approach with the aid of queue, each time extract and comp[are values of two nodes. O(n) / O(n)
        queue = deque([root, root])

        while queue:
            l, r = queue.popleft(), queue.popleft()
            if not l and not r:
                continue
            elif (not l or not r) or (l.val != r.val):
                return False
            # queue first in first out, so from left to right of each level 
            # thus, first l.left and then l.right
            queue += [l.left, r.right, l.right, r.left]
        return True

if __name__ == '__main__':
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(2)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    print(Solution().isSymmetric(root))