class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = collections.defaultdict(list)
        for i, m in enumerate(manager):
            if m >= 0:
                children[m].append(i)
        return self.dfs(headID, children, informTime)

    def dfs(self, head, children, informTime):
        if head not in children:
            return 0
        maxTime = 0
        for child in children[head]:
            time = self.dfs(child, children, informTime)
            maxTime = max(maxTime, time)
        return maxTime+informTime[head]
