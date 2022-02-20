class Solution:
    '''
    考察转换 n进制的方法
    '''
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = 0
        if num< 0:
            negative = 1
            num = abs(num)
        result = ""
        while num > 0:
            digit = num%7
            result = str(digit) + result
            num //= 7
        if negative:
            result = '-' + result
        return result