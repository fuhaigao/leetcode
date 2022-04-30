class Solution:
    '''
    Observation 1: when we move a digit to left, other digit are shifted to right. i.e 432 got shifted to right by 1.
    Observation 2: Choose first smallest d that is in reach of k.
    '''

    def minInteger(self, num: str, k: int) -> str:
        preInd = 0
        to_find = 0
        while k > 0 and to_find < 10 and preInd < len(num):
            ind = num.find(str(to_find), preInd)
            if ind != -1 and ind - preInd <= k:
                # swap and reroder numbers
                num = num[:preInd] + num[ind] + num[preInd:ind] + num[ind+1:]
                to_find = 0
                k = k - ind + preInd
                preInd += 1
            else:
                to_find += 1
        return num
