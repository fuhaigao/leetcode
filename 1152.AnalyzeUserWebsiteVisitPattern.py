class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = collections.defaultdict(list)
        for user, time, website in sorted(zip(username, timestamp, website), key = lambda x: (x[0],x[1])):
            visits[user].append(website)
        counter = collections.Counter()
        for user, websites in visits.items():
#             combinations = Combination(3).getCombinations(websites)
#             for combination in set(combinations):
#                 counter[combination] += 1
            for triple in set(itertools.combinations(websites, 3)):
                counter[triple]+=1
        
        result, maxCount = list(), 0
        for combination, count in counter.items():
            if count > maxCount:
                result, maxCount = combination, count
            elif count == maxCount and result > combination:
                result = combination
        return result
            

class Combination:
    def __init__(self, length):
        self.results = []
        self.length = length
    def getCombinations(self, items):
        for i in range(len(items)):
            self.backtracking(items, i, [])
        return [tuple(item) for item in self.results]
    
    def backtracking(self, items, index, curr):
        if len(curr) == self.length and curr not in self.results:
            self.results.append(curr)
            return
        for i in range(index, len(items)):
            self.backtracking(items, index+1, curr+[items[index]])