class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: (-x[1], -x[0]))
        res = 0
        i = 0
        while truckSize > 0 and i < len(boxTypes):
            res += min(truckSize, boxTypes[i][0]) * boxTypes[i][1]
            truckSize -= boxTypes[i][0]
            i += 1
        return res