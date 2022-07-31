class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = [[0,1], [1,0], [0,-1], [-1,0]]
        i = 0
        x, y = 0, 0
        for ins in instructions:
            if ins == "R":
                i = (i+1)%4
            elif ins == "L":
                i = (i+3)%4
            else:
                x, y = x+direction[i][0], y+direction[i][1]
        return (x==0 and y==0) or i > 0