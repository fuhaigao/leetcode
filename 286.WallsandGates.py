class Solution:
    # BFS
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        deque = collections.deque()
        visited = set()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    deque.append((i, j))
                    visited.add((i, j))

        level = 0
        while deque:
            level += 1
            for _ in range(len(deque)):
                x, y = deque.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    currX, currY = x+dx, y+dy
                    if currX < 0 or currX >= len(rooms) or currY < 0 or currY >= len(rooms[0]) or (currX, currY) in visited or rooms[currX][currY] == -1:
                        continue
                    visited.add((currX, currY))
                    rooms[currX][currY] = level
                    deque.append((currX, currY))
        return
