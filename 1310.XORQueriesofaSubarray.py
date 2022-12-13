class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [0] * len(arr)
        for i in range(len(arr)):
            if i == 0:
                xors[i] = arr[i]
            else:
                xors[i] = xors[i-1] ^ arr[i]
                
        res = []
        for left, right in queries:
            if left == 0:
                res.append(xors[right])
            else:
                res.append(xors[left-1]^xors[right])
        return res