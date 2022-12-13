class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        dist = collections.defaultdict(int)
        dist[startGene] = 0
        queue = collections.deque([startGene])
        
        while queue:
            gene = queue.popleft()
            if gene == endGene:
                return dist[gene]
            for nextGene in bank:
                if not nextGene in dist and self.isValidMutation(gene, nextGene):
                    dist[nextGene] = dist[gene] + 1
                    queue.append(nextGene)
        return -1
        
    
    def isValidMutation(self, a, b):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[:i] == b[:i] and a[i+1:] == b[i+1:]:
                return True
        return False
    
        # alternative way to check
        # return sum([1 for i in range(len(a)) if a[i]!=b[i]]) == 1