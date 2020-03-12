# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
# reservoir sampling solution
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.node = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        index, res, curr = 1, self.node, self.node.next
        while curr:
            if random.randint(0, index) is 0:
                res = curr
            curr = curr.next
            index += 1
        return res.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()