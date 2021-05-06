from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
       
        """
        First, intuition is BFS, traverse the tree level by level

        [3] Odd level
        [9 20] --> [20 9] Even level pop from the last
        [15 7] --> [15 7] Odd level
        using stack to pop from the back
        """
        l1, l2, level, result = [root], [], [], [] # odd / even level with Treenode / level with value

        while l1 or l2:
            while l1:
                node = l1.pop() 
                level.append(node.val)
                if node.left:
                    l2.append(node.left)
                if node.right:
                    l2.append(node.right)
            # one level ended, append to the result and clear the level
            if level:
                result.append(level)
                level = []
                
            while l2:
                node = l2.pop()
                level.append(node.val)
                if node.right:
                    l1.append(node.right)
                if node.left:
                    l1.append(node.left)
            if level:
                result.append(level)
                level = []

        return result

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().zigzagLevelOrder(root))