# https://leetcode.com/problems/cyclically-rotating-a-grid/discuss/1299663/Inplace-or-Intuitive-and-Easy-or-4-pointer-(TBLR)-or-Detailed-Explanation
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        top, right, bot, left = 0, len(grid[0])-1, len(grid)-1, 0
        while top < bot and left < right:
            layerCount = 2*(bot-top+1) + 2*(right-left+1) - 4
            count = k % layerCount
            while count > 0:
                tmp = grid[top][left]
                for i in range(left, right):
                    grid[top][i] = grid[top][i+1]
                for i in range(top, bot):
                    grid[i][right] = grid[i+1][right]
                for i in range(right, left, -1):
                    grid[bot][i] = grid[bot][i-1]
                for i in range(bot, top, -1):
                    grid[i][left] = grid[i-1][left]
                grid[top+1][left] = tmp
                count -= 1

            top, right, bot, left = top+1, right-1, bot-1, left+1
        return grid
