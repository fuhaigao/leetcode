class Solution:
    # 找规律，use counter
    def originalDigits(self, s: str) -> str:
        counter = Counter(s)
        number2Word = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
                   5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
        # letter to uniquely select each number.
        number2Target = {0: 'z', 2: 'w', 4: 'u', 6: 'x', 8: 'g',
                        1: 'o', 3: 't', 5: 'f', 7: 's', 9: 'i'}
        numberOfWords = [0]*10
        for i in [0,2,4,6,8,1,3,5,7,9]:
            target = number2Target[i]
            word = number2Word[i]
            if counter[target]:
                numberOfWords[i] = counter[target]
                for c in word:
                    counter[c] -= numberOfWords[i]
        result = ""
        for i in range(len(numberOfWords)):
            result += numberOfWords[i]*str(i)
        return result