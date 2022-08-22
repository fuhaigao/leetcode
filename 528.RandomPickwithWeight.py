class Solution:
    # Frequency Sum
    def __init__(self, w: List[int]):
        self.weights = []
        self.sums = 0
        for weight in w:
            self.sums += weight
            self.weights.append(self.sums)

    def pickIndex(self) -> int:
        target=random.randint(1, self.sums)
        # O (n), can be optimized to O(logn) with binary search
        # for i in range(len(self.weights)):
        #     if self.weights[i] >= target:
        #         return i
        left, right = 0, len(self.weights)-1
        while left < right:
            mid = (left+right)//2
            if self.weights[mid] < target:
                left = mid + 1
            elif self.weights[mid] > target:
                right = mid
            else:
                return mid
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()