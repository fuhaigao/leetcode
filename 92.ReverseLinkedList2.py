# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev, start, last = dummy, head, head
        for i in range(left-1):
            prev = prev.next
            start = start.next
            last = last.next
        for i in range(right-left+1):
            last = last.next

        for i in range(right-left+1):
            tmp = start.next
            start.next = last
            last = start
            start = tmp
        prev.next = last
        return dummy.next

