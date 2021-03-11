# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # use count because:
    # it handles the case of a "tie" when two list nodes have the same value. When that happens, Python will look at the next value in the tuple (in this case, count), and sort based on that value. Without count, a "tie" would error out if the next value in the tuple were a ListNode (which can't be compared).
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = []
        dummy = ListNode(0)
        curr = dummy
        count = 0
        for node in lists:
            if node:
                count += 1
                heapq.heappush(pq, (node.val, count, node))
        while len(pq) > 0:
            currMin = heapq.heappop(pq)
            curr.next = currMin[2]
            curr = curr.next
            if curr.next:
                count += 1
                heapq.heappush(pq, (curr.next.val, count, curr.next))
        return dummy.next
   