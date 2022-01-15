class Solution:
    '''
    Greedy
    https://programmercarl.com/0135.%E5%88%86%E5%8F%91%E7%B3%96%E6%9E%9C.html#%E6%80%9D%E8%B7%AF
    
    Step 1: from left to right, if ratings[i+1] > ratings[i] then candies[i+1] = candies[i] + 1
    Step 2: from right to left, if ratings[i-1] > ratings[i] then candies[i-1] = max(candies[i-1], prevChildCandy+1)
    '''
    def candy(self, ratings: List[int]) -> int:
        candies = [0]*len(ratings)
        candies[0] = 1
        # Step 1
        for i in range(len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                candies[i+1] = candies[i]+1
            else:
                candies[i+1] = 1
        
        #Step 2
        prevChildCandy = 1
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i-1], prevChildCandy+1)
            prevChildCandy = candies[i-1]
        return sum(candies)