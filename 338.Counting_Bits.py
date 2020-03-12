class Solution:
    def countBits(self, num: int) -> List[int]:
        offset = 1
        result = [0]
        for i in range(1, num+1):
            if offset*2 == i:
                offset *= 2
            result.append(result[i-offset]+1)
        return result