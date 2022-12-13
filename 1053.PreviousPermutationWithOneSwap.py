class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        firstLarger = -1
        for i in range(len(arr)-1, 0, -1):
            if arr[i] < arr[i-1]:
                firstLarger = i-1
                break

        if firstLarger == -1:
            return arr

        # find the largest value that is smaller than arr[firstLarger], swap them to get the largest permutation that is smaller than arr
        # Since arr[firstLarger+1:] is increasing order, we can simply find from the end
        for i in range(len(arr)-1, firstLarger, -1):
            if arr[i] < arr[firstLarger] and arr[i] != arr[i-1]:
                arr[i], arr[firstLarger] = arr[firstLarger], arr[i]
                break
        return arr
