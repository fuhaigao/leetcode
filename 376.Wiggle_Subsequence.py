class Solution:
    '''
    greedy
    局部最优：删除单调坡度上的节点（不包括单调坡度两端的节点），那么这个坡度就可以有两个局部峰值。
    整体最优：整个序列有最多的局部峰值，从而达到最长摆动序列。
    '''
    def wiggleMaxLength(self, nums: List[int]) -> int:
        res, preC = 1, 0
        for i in range(1, len(nums)):
            currC = nums[i] - nums[i-1]
            if currC * preC <= 0 and currC != 0:
                res += 1
                preC = currC            
        return res
            