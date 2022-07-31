class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        left, right = 0, 0
        slots1.sort(key = lambda x: (x[0], x[1]))
        slots2.sort(key = lambda x: (x[0], x[1]))
        while left < len(slots1) and right < len(slots2):
            intervalL, intervalR = slots1[left], slots2[right]
            if intervalR[0] < intervalL[1] or intervalL[0] < intervalR[1]:
                start, end = max(intervalL[0], intervalR[0]), min(intervalL[1], intervalR[1])
                if end - start >= duration:
                    return [start, start+duration]
            if intervalL[1] < intervalR[1]:
                left += 1
            else:
                right += 1
        return []