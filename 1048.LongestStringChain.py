class Solution:
    '''
    DP Question
    global maximum keep update the longest chain
    We need to check all words that shorter than current word (any shorter word is possibly a predecessor). Use a dictionary to keep track the chain for traversed word
    '''
    def longestStrChain(self, words: List[str]) -> int:
        wordToChain = dict()
        words.sort(key=lambda x:len(x))
        print(words)
        result = 1
        for word in words:
            wordToChain[word] = 1
            for i in range(len(word)):
                possiblePrecessor = word[:i]+word[i+1:len(word)]
                print(possiblePrecessor)
                if possiblePrecessor in wordToChain:
                    wordToChain[word] = wordToChain[possiblePrecessor]+1
                    result = max(result, wordToChain[word])
        return result
                