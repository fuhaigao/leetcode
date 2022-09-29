class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        width = sum(wall[0])
        edges = collections.defaultdict(int)
        maxEdges = 0
        for row in wall:
            index = 0
            for brick in row[:-1]:
                index += brick
                edges[index] += 1
                maxEdges = max(maxEdges, edges[index])
            # Use accumulate() instead
            # for index in accumulate(row[:-1]):
            #     edges[index] += 1
            #     maxEdges = max(maxEdges, edges[index])
        return len(wall) - maxEdges
