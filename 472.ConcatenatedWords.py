class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)

        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in wordSet and suffix in wordSet:
                    return True
                if prefix in wordSet and dfs(suffix):
                    return True
                if suffix in wordSet and dfs(prefix):
                    return True
            return False

        result = []
        for word in words:
            if dfs(word):
                result.append(word)
        return result
