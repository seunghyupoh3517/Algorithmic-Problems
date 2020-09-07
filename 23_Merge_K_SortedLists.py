""" https://leetcode.com/problems/merge-k-sorted-lists/
Given an array of linked-lists lists, each linked list is sorted in ascending order.
Merge all the linked-lists into one sort linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        # Brute Force, traverse all the linked lists and get all the values, sort, put all the value into new sorted linked list
        # O(NlogN) time, O(N) Space, -  N: # of Nodes
        nodes = []
        head = point = ListNode(0)

        for s in lists:
            while s:
                nodes.append(s.val)
                s = s.next
        # sorted - returns sorted in ascending order
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next

        return head.next
        """
        
        # Doing the comparison process by priority queue
        # O(Nlogk) time, O(N) Space, - k: # of linked lists
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next

if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(4)
    list1.next.next = ListNode(5)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    list3 = ListNode(2)
    list3.next = ListNode(6)
    #lists = [[1,4,5],[1,3,4],[2,6]]
    head = Solution().mergeKLists([list1, list2, list3])
    
    while head is not None:
        print(head.val)
        head = head.next