
class Solution:
    def __init__(self, nums):
        list_idx = 0
        self.nums = []
        while any(nums):
            i = list_idx % len(nums)
            if nums[i]:
                self.nums.append(nums[i].pop(0))
            list_idx += 1

    def __iter__(self):
        return SolIterator(self)


class SolIterator:
    def __init__(self, nums):
        self._nums = nums
        self.index = 0

    def __next__(self):
        if self.index < len(self._nums.nums):
            result = self._nums.nums[self.index]
            self.index += 1
            return result
        raise StopIteration


# iterator = SolIterator([[1, 2], [4], [6], [], [7, 8, 9]])
# print("================== iteration 1 =================")
# while True:
#     try:
#         elem = next(iterator)
#         print(elem)
#     except StopIteration:
#         break

print("================== iteration 1 =================")
sol = Solution([[1, 2], [4], [6], [], [7, 8, 9]])
for num in sol:
    print(num)
