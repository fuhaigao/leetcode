class Solution:
    def alienOrder(self, words: List[str]) -> str:
        map = collections.defaultdict(set)
        degree = collections.defaultdict(int)

        for word in words:
            for l in word:
                degree[l] = 0

        for i in range(len(words)-1):
            currWord = words[i]
            nextWord = words[i+1]
            length = min(len(currWord), len(nextWord))
            for j in range(length):
                if currWord[j] != nextWord[j]:
                    if nextWord[j] not in map[currWord[j]]:
                        map[currWord[j]].add(nextWord[j])
                        degree[nextWord[j]] += 1
                    break
                elif j == length-1 and len(currWord) > len(nextWord):
                    return ""

        queue = []
        for key in degree.keys():
            val = degree[key]
            if val == 0:
                queue.append(key)

        result = ""
        while queue:
            letter = queue.pop(0)
            for neighbour in map[letter]:
                degree[neighbour] -= 1
                if degree[neighbour] == 0:
                    queue.append(neighbour)
            result += letter
        print(len(map))
        if len(result) != len(map):
            return ""
        return result
