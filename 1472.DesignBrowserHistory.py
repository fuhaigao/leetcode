
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.idx = 0
        self.bound = 0

    def visit(self, url: str) -> None:
        self.idx += 1
        if self.idx == len(self.history):
            self.history.append(url)
        self.history[self.idx] = url
        self.bound = self.idx

    def back(self, steps: int) -> str:
        self.idx = max(self.idx-steps, 0)
        return self.history[self.idx]

    def forward(self, steps: int) -> str:
        self.idx = min(self.idx+steps, self.bound)
        return self.history[self.idx]



#Doule Pointer, not efficient enough
# class BrowserHistory:
#     def __init__(self, homepage: str):
#         self.head = Node(homepage)
#         self.curr = self.head

#     def visit(self, url: str) -> None:
#         curr = Node(url)
#         self.curr.next = curr
#         curr.prev = self.curr
#         self.curr = curr

#     def back(self, steps: int) -> str:
#         # print(self.curr.val, self.curr.prev.val)
#         while steps > 0 and self.curr.prev:
#             self.curr = self.curr.prev
#             steps -= 1
#         return self.curr.val

#     def forward(self, steps: int) -> str:
#         while steps > 0 and self.curr.next:
#             self.curr = self.curr.next
#             steps -= 1
#         return self.curr.val

# class Node:
    
#     def __init__(self, value):
#         self.val = value
#         self.prev = None
#         self.next = None

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)