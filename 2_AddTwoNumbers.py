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

        # Brute force - not considering carried 1 
        """
        x1 = l1.val + l2.val
        l3 = ListNode(x1)

        x2 = l1.next.val + l2.next.val 
        l3.next = ListNode(x2)

        x3 = l1.next.next.val + l2.next.next.val
        l3.next.next = ListNode(x3)

        return l3
        """

        carry = 0
        output = ListNode(0)
        output_tail = output

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            sum = val1 + val2 + carry
            carry, remainder = divmod(sum, 10)

            output_tail.next = ListNode(remainder)
            output_tail = output_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)


        return output.next


if __name__ == '__main__':
    #l1 = [2,4,3] 
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    #l2 = [5,6,4]
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    l3 = (Solution().addTwoNumbers(l1, l2))

    output = []
    while l3 is not None:
        output.append(l3.val)
        l3 = l3.next

    print(output)

    
