# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        last, curr, prev = head, head, dummy
        for i in range(right):
            if i < left-1:
                prev = prev.next
                curr = curr.next
            last = last.next

        for i in range(right-left+1):
            tmp = curr.next
            curr.next = last
            last, curr = curr, tmp
        prev.next = last
        return dummy.next
