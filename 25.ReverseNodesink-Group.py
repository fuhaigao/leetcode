# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr, count = head, 0
        while curr and count != k:
            curr = curr.next
            count += 1
        if count == k:
            last = self.reverseKGroup(curr, k)
            # reverse linked list
            currHead = head
            for _ in range(count):
                tmp = currHead.next
                currHead.next = last
                last = currHead
                currHead = tmp
            return last
        else:
            return head