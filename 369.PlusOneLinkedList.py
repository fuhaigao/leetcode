# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if (self.dfs(head) == 0):
            return head
        dummy = ListNode(1)
        dummy.next = head
        return dummy
        
    def dfs(self, node):
        if not node:
            return 1
        carry = self.dfs(node.next)
        if carry == 0:
            return 0
    
        val = node.val + 1
        node.val = val%10;
        return val//10;