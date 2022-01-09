# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        pre = dummy
        while head:
            nextNode = head.next
            while pre.next and pre.next.val < head.val:
                pre = pre.next
            head.next = pre.next
            pre.next = head
            pre = dummy
            head = nextNode
        return dummy.next