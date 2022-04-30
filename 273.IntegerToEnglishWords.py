class Solution:
    def __init__(self):
        self.LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                             "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.TENS = ["", "Ten", "Twenty", "Thirty", "Forty",
                     "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.THOUSANDS = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        thousands_idx = 0
        res = ""
        while num > 0:
            if num % 1000 != 0:
                words = self.getWords(num % 1000)
                res = words + self.THOUSANDS[thousands_idx] + ' ' + res
            num //= 1000
            thousands_idx += 1
        return res.strip()

    def getWords(self, num):
        if num == 0:
            return ""
        if num < 20:
            return self.LESS_THAN_20[num] + ' '
        elif num < 100:
            return self.TENS[num//10] + ' ' + self.getWords(num % 10)
        else:
            return self.LESS_THAN_20[num//100] + " Hundred " + self.getWords(num % 100)
