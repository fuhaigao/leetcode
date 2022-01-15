class Solution:
    '''
    Greedy
    https://programmercarl.com/0738.%E5%8D%95%E8%B0%83%E9%80%92%E5%A2%9E%E7%9A%84%E6%95%B0%E5%AD%97.html#%E6%9A%B4%E5%8A%9B%E8%A7%A3%E6%B3%95
    - number switch to str list to modify each bit
    - 局部最优：遇到strNum[i-1] > strNum[i]的情况，让strNum[i-1]--，然后strNum[i:]更新为9，可以保证数字变成最大单调递增整数。
    - 全局最优：得到小于等于N的最大单调递增的整数。
    '''
    def monotoneIncreasingDigits(self, n: int) -> int:
        nStr = list(str(n))
        for i in range(len(nStr)-1, 0, -1):
            if nStr[i] < nStr[i-1]:
                nStr[i:] = '9'*(len(nStr)-i)
                nStr[i-1] = str(int(nStr[i-1])-1)
        return int(''.join(nStr))