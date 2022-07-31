# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
#         stack = []
#         l = 0
#         curr = head
#         while curr:
#             l += 1
#             curr = curr.next
#         res = [0]*l
#         i = 0
#         while head:
#             while stack and stack[-1][1] < head.val:
#                 res[stack.pop()[0]] = head.val
#             stack.append((i, head.val))
#             i += 1
#             head = head.next
#         while stack:
#             res[stack.pop()[0]] = 0
#         return res
    
    ## optimize: no need to calculate length first, can pre-set to 0 each time and alter later
        stack, res = [], []
        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            stack.append((len(res), head.val))
            res.append(0)
            head = head.next
        return res
            