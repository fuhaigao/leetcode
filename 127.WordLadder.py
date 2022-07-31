class Solution:
    # Simple BFS
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        queue, visit = deque([beginWord]), set(beginWord)
        # improve performance when check word exists in wordList
        wordList = set(wordList)
        changes = 1
        alph = "abcdefghijklmnopqrstuvwxyz"

        while queue:
            changes += 1
            for i in range(len(queue)):
                currWord = queue.popleft()
                for i in range(len(currWord)):
                    prefix, suffix, = currWord[:i], currWord[i+1:]
                    for letter in alph:
                        replacedWord = prefix + letter + suffix
                        if replacedWord in wordList and replacedWord not in visit:
                            if replacedWord == endWord:
                                return changes
                            visit.add(replacedWord)
                            queue.append(replacedWord)
        return 0
