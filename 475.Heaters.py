class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        radius = float('-inf')
        heaters.sort()
        for house in houses:
            # idx = bisect.bisect_right(heaters,house)
            idx = self.findIndex(heaters, house)
            distToLeftHeater, distToRightHeater = float('inf'), float('inf')
            if idx > 0:
                distToLeftHeater = house - heaters[idx-1]
            if idx < len(heaters):
                distToRightHeater = heaters[idx] - house
            radius = max(radius, min(distToLeftHeater, distToRightHeater))
        return radius
    
    def findIndex(self, heaters, house):
        left, right = 0, len(heaters)-1
        while left <= right:
            mid = (left+right)//2
            if heaters[mid] == house:
                return mid
            elif house > heaters[mid]:
                left = mid+1
            else:
                right = mid-1
        return max(left,right)