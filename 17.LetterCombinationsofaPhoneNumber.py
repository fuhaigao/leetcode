class Solution:
    def __init__(self):
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.res = []
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.backtracking("", digits)
        return self.res
    def backtracking(self, path, digits):
        if len(digits) == 0:
            self.res.append(path)
        else:
            for i in range(len(self.letter_map[digits[0]])):
                letter = self.letter_map[digits[0]][i]
                self.backtracking(path+letter, digits[1:])
        return