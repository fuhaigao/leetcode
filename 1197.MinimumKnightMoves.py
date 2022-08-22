class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        # no need for (-1,-2) and (-2,-1)
        directions = [[2,1], [2,-1], [1,2], [1,-2], [-2,1], [-1,2]]     
        queue = collections.deque([(0,0)])
        level = 0
        visited = set([(0,0)])
        while queue:
            size = len(queue)
            for _ in range(size):
                pos_x, pos_y = queue.popleft()
                if pos_x == x and pos_y == y:
                    return level
                for i,j in directions:
                    if (pos_x+i, pos_y+j) not in visited and -1 <= pos_x+i <= x+2 and -1<= pos_y+j <= y+2:
                        visited.add((pos_x+i, pos_y+j))
                        queue.append([pos_x+i, pos_y+j])
            level += 1