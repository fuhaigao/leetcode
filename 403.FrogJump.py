class Solution:
#     DFS TLE
#     def canCross(self, stones: List[int]) -> bool:
#         return self.dfs(1, 0, stones)
    
#     def dfs(self, step, index, stones):
#         if stones[index] + step == stones[-1]:
#             return True
#         # if stones[index] + step < stones[index+1]:
#         #     return False
#         reach = stones[index] + step
#         for i in range(index+1, len(stones)):
#             if stones[i] == reach:
#                 return self.dfs(step-1, i, stones) or self.dfs(step, i, stones) or self.dfs(step+1, i, stones)
#             if stones[i] > reach:
#                 return False
                
    def canCross(self, stones: List[int]) -> bool:
        stoneSteps = dict()
        for stone in stones:
            stoneSteps[stone] = set()
        stoneSteps[stones[0]].add(1)
        for stone in stones:
            for step in stoneSteps[stone]:
                reach = stone + step
                if reach == stones[-1]:
                    return True
                if reach in stoneSteps:
                    stoneSteps[reach].add(step)
                    stoneSteps[reach].add(step+1)
                    if step > 1:
                        stoneSteps[reach].add(step-1)

        return False