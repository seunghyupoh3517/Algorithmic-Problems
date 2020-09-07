"""https://leetcode.com/problems/add-two-numbers-ii/
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = point = ListNode(0)
        if not l1 and not l2:
            return None
        
        l1_num = 0
        while l1:
            l1_num = l1_num * 10 + l1.val
            l1 = l1.next
        
        l2_num = 0
        while l2:
            l2_num = l2_num * 10 + l2.val
            l2 = l2.next

        sum = l1_num + l2_num
        for value in str(sum):
            point.next = ListNode(value)
            point = point.next
        
        return head.next

if __name__ == '__main__':
    list1 = ListNode(7)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list1.next.next.next = ListNode(3)

    list2 = ListNode(5)
    list2.next = ListNode(6)
    list2.next.next = ListNode(4)

    head = Solution().addTwoNumbers(list1, list2)
    while head is not None:
        print(head.val)
        head = head.next
