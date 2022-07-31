class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        def dist(point):
            return abs(point[0]-rCenter) + abs(point[1]-cCenter)
        
        points = [(x, y) for x in range(rows) for y in range(cols)]
        points.sort(key=dist)
        return points