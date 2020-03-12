class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(min(len(matrix[0]), k)):
            curr = (matrix[0][i], 0, i)
            heapq.heappush(heap, curr)
        numberCount, number = 0, 0
        while k > 0:
            number, row, col = heapq.heappop(heap)
            k -= 1
            if row == len(matrix)-1: 
                continue
            next_val = (matrix[row+1][col], row+1, col)
            heapq.heappush(heap, next_val)
        return number