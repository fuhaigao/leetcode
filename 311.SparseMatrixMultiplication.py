class Solution:
    # def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
    #     res = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    #     for i in range(len(mat1)):
    #         for j in range(len(mat1[0])):
    #             for k in range(len(mat2[0])):
    #                 res[i][k] += mat1[i][j] * mat2[j][k]
    #     return res
    
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        row1, col1, row2, col2 = len(mat1), len(mat1[0]), len(mat2), len(mat2[0])
        map1, map2 = collections.defaultdict(list), collections.defaultdict(list)
        for i in range(row1):
            for j in range(col1):
                if mat1[i][j] != 0:
                    map1[i].append([j, mat1[i][j]])
        
        for j in range(col2):
            for i in range(row2):
                if mat2[i][j] != 0:
                    map2[j].append([i, mat2[i][j]])
                    
        print(map1, map2)        
        res = [[0 for _ in range(col2)] for _ in range(row1)]
        for i in range(row1):
            for j in range(col2):
                res[i][j] = self.dotOperation(map1[i], map2[j])
        return res
        
    def dotOperation(self, row, col):
        print(row, col)
        p1, p2 = 0, 0
        res = 0
        while p1 < len(row) and p2 < len(col):
            idx1, idx2 = row[p1][0], col[p2][0]
            print(idx1, idx2)
            if idx1 == idx2:
                res += row[p1][1] * col[p2][1]
                p1 += 1
                p2 += 1
            elif idx1 < idx2:
                p1 += 1
            else:
                p2 += 1
        return res