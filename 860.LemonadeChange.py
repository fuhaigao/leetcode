class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveChange = 0
        tenChange = 0
        for num in bills:
            if num == 5:
                fiveChange += 1
            elif num == 10:
                fiveChange -= 1
                tenChange += 1
            else:
                if tenChange:
                    tenChange -= 1
                    fiveChange -= 1
                else:
                    fiveChange -=3
            if fiveChange < 0:
                return False
        return True