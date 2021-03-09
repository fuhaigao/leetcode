# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # split into two lists
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        
        # reverse the second list
        curr = mid
        last = None
        while curr:
            currNext = curr.next
            curr.next = last
            last = curr
            curr = currNext
        
        first = head
        second = last
        
        # merge two list:
        # 1->2->3  6->5->4. => 1->6->2->5->4->3
        while first and second:
            tmp = first.next
            first.next = second
            second = tmp
            first = first.next
        return head