class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            daysNeed = 1
            currCapacity = 0
            for w in weights:
                if currCapacity + w > mid:
                    currCapacity = 0
                    daysNeed += 1
                currCapacity += w
            if daysNeed > days:
                left = mid + 1
            else:
                right = mid
        return left