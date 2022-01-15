class Solution:
    # Greedy
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0],x[1]))
        curr, index, count = 0, 0, 0
        while curr < len(points):
            count += 1
            right = float('inf')
            while index < len(points) and points[index][0] <= right:
                right = min(right, points[index][1])
                index += 1
            curr = index
        return count