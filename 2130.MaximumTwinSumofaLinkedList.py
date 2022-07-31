# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # nodeList = []
        # curr = head
        # while curr:
        #     nodeList.append(curr.val)
        #     curr = curr.next
        # l, r = 0, len(nodeList)-1
        # res = 0
        # while l < r:
        #     res = max(res, nodeList[l]+nodeList[r])
        #     l += 1
        #     r -= 1
        # return res
    
    #optimize with O(1) space
        def reverse(head):
            prev, curr = None, head
            while curr:
                nextNode = curr.next
                curr.next = prev
                prev, curr = curr, nextNode
            return prev
            
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first, second = head, reverse(slow)
        res = 0
        while second:
            print(first.val, second.val)
            res = max(res, first.val + second.val)
            first = first.next
            second = second.next
        return res