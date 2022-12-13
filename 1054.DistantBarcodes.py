class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = collections.Counter(barcodes)
        res = [0]*len(barcodes)
        occurences = sorted(counter.items(), key=lambda x: -x[1])
        idx = 0
        for val, occurence in occurences:
            while occurence:
                res[idx] = val
                occurence -= 1
                idx += 2
                if idx >= len(barcodes):
                    idx = 1
        return res
