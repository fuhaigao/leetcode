class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        left, right = 0, (row*col)-1
        while left < right:
            mid = (left+right) // 2
            val = matrix[mid//col][mid % col]
            if val == target:
                return True
            elif target > val:
                left = mid+1
            else:
                right = mid
        return matrix[left//col][left % col] == target
