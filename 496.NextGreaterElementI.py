class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = {}
        stack = [nums2[0]]
        for i in range(1, len(nums2)):
            while stack and stack[-1] < nums2[i]:
                key = stack.pop()
                nextGreater[key] = nums2[i]
            stack.append(nums2[i])
        result = []
        for num in nums1:
            val = nextGreater.get(num, -1)
            result.append(val)
        return result