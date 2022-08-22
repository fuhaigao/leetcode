class Solution:
    # Solution without using mod operator, since mod is slower than plus
    def fizzBuzz(self, n: int) -> List[str]:
        base3, base5, base15 = 3, 5, 15
        res = []
        for i in range(1, n+1):
            if i == base15:
                res.append("FizzBuzz")
                base3 += 3
                base5 += 5
                base15 += 15
            elif i == base3:
                res.append("Fizz")
                base3 += 3
            elif i == base5:
                res.append("Buzz")
                base5 += 5
            else:
                res.append(str(i))
        return res