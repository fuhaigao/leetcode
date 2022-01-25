class Solution:
    '''
    Compared to Q215:
    因为要return all top k frequent words, 所以 running time of heap is similar to quick sort
    '''
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pq = []
        wordToCount = collections.defaultdict(int)
        result = []
        for i in range(len(words)):
            wordToCount[words[i]] += 1
        for word in wordToCount:
            count = wordToCount[word]
            heapq.heappush(pq, (-count, word))
        while k > 0:
            count, word = heapq.heappop(pq)
            result.append(word)
            k -= 1
                
        return result
            