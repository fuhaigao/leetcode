class Solution:
    '''
    n = (x+x+m-1)*(m/2)
    calculate x based on m OR calculate m based on x
    eaiser for x based on m:
    x = n/m - m/2 + 1/2
    x = (2n-m*m+m)/(2m)
    At this point, m must smaller than sqrt(2n)
    '''
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        m = 1
        while m < sqrt(2*n):
        # for m in range(1, sqrt(2*n)):
            if (2*n-m*m+m) % (2*m) == 0 :
                count += 1
            m += 1
        return count