'''
Two approaches for different trade off:
1. quick find (when read is more than write)
2. quick add (when write is more than read)
'''

# quick find
# class TwoSum:

#     def __init__(self):
#         self.sums = set()
#         self.nums = set()

#     def add(self, number: int) -> None:
#         for num in self.nums:
#             self.sums.add(num+number)
#         self.nums.add(number)

#     def find(self, value: int) -> bool:
#         return value in self.sums


# quick add
class TwoSum:

    def __init__(self):
        self.d = collections.defaultdict(int)

    def add(self, number: int) -> None:
        self.d[number] += 1

    def find(self, value: int) -> bool:
        for key in self.d:
            target = value - key
            if target == key and self.d[key] > 1:
                return True
            if target != key and target in self.d:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
