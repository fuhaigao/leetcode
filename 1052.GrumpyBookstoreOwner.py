class Solution:
    # Sliding Window
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        start, maxSatisfied, currSatisfied = 0, 0, 0
        nonGrumpySum = 0
        for i in range(len(customers)):
            # use sliding window to find the best place to apply "minutes"
            if grumpy[i] == 1:
                currSatisfied += customers[i]
            if i - start + 1 > minutes:
                if grumpy[start] == 1:
                    currSatisfied -= customers[start]
                start += 1
            maxSatisfied = max(maxSatisfied, currSatisfied)

            # keep track non-grumpy value
            if grumpy[i] == 0:
                nonGrumpySum += customers[i]
        return nonGrumpySum + maxSatisfied
