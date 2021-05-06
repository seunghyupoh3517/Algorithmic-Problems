# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        # Comparing the nodes from root, left, right O(N*M) time / O(M) space
        def check(s_t, t_t):
            if s_t is None and t_t is None:
                return True
            if s_t is None or t_t is None:
                return False
            return (s_t.val == t_t.val) and check(s_t.left, t_t.left) and check(s_t.right, t_t.right)

        if not s:
            return False
        
        # helper fuction to recursively go check l, r branches
        if check(s, t):
            return True
        
        # whether the t is s left subtree or right subtree
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)