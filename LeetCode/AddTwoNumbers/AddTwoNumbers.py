# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object): # My take on this
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        x = self.getNumber(l1)
        y = self.getNumber(l2)

        solution = map(int, str(x + y))
        
        return self.arrToListNode(solution)
    
    def arrToListNode(self, arr):
        head = None
        for num in arr:
            head = ListNode(num, head)
        return head


    def getNumber(self, node):
        array = []
        current = node
        value = 0
        temp = 0
        while current:
            array.append(current.val)
            current = current.next

        for i, num in enumerate(array):
             temp = num * 10**i
             value += temp
    
        return value
        


# Best practice solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class BestPractice(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            value = total % 10

            current.next = ListNode(value)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
        