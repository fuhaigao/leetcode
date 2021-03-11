class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        cut1, cut2 = 0, 0
        l, r = 0, len(nums1)
        length = len(nums1) + len(nums2)

        while l <= r:
            cut1 = (l+r)//2
            cut2 = length//2 - cut1
            l1 = nums1[cut1-1] if cut1 > 0 else -1
            l2 = nums2[cut2-1] if cut2 > 0 else -1
            r1 = nums1[cut1] if cut1 < len(nums1) else float('inf')
            r2 = nums2[cut2] if cut2 < len(nums2) else float('inf')  

            if l1 > r2:
                r = cut1-1
            elif l2 > r1:
                l = cut1+1      
            else:
                if length % 2 == 0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return min(r1,r2)
        return -1
