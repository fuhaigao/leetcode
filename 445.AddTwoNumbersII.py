# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        res = None
        carry = 0
        while stack1 and stack2:
            val = carry + stack1.pop() + stack2.pop()
            node = ListNode(val%10)
            node.next = res
            res = node
            carry = val//10
        
        while stack1:
            val = carry + stack1.pop()
            node = ListNode(val%10)
            node.next = res
            res = node
            carry = val//10
        
        while stack2:
            val = carry + stack2.pop()
            node = ListNode(val%10)
            node.next = res
            res = node
            carry = val//10
        
        if carry == 1:
            node = ListNode(1)
            node.next = res
            return node
        return res