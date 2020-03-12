class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        res = []
        if (input.isdigit()):
            return [int(input)]
        for i in range(len(input)):
            if input[i] in "+-*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for num1 in left:
                    for num2 in right:
                        res.append(self.calculate(num1, num2, input[i]))
        return res
    def calculate(self, num1, num2, op):
        if op == "+":
            return num1 + num2
        if op == "-":
            return num1 - num2
        if op == "*":
            return num1 * num2