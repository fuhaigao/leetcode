class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count = [0] * 10
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if count[int(secret[i])] > 0:
                    cows += 1
                if count[int(guess[i])] < 0:
                    cows +=1
                count[int(secret[i])] -= 1
                count[int(guess[i])] += 1
        return "{}A{}B".format(bulls,cows)